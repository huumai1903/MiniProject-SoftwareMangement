#!/usr/bin/env python3
"""
Facebook Post Cleanup Tool
- Xoá tất cả bài SHARE từ năm TARGET_YEAR
- Đặt bài TỰ VIẾT từ năm TARGET_YEAR sang chế độ Chỉ mình tôi
"""

import os
import sys
import time
import random
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

load_dotenv()

FB_EMAIL    = os.getenv("FB_EMAIL", "")
FB_PASSWORD = os.getenv("FB_PASSWORD", "")
TARGET_YEAR = int(os.getenv("TARGET_YEAR", "2013"))
DELAY       = float(os.getenv("DELAY_BETWEEN_ACTIONS", "2"))
HEADLESS    = os.getenv("HEADLESS", "false").lower() == "true"

ACTIVITY_LOG_URL = "https://www.facebook.com/profile/timeline/activity"


def human_delay(base: float = DELAY) -> None:
    """Thêm thời gian chờ ngẫu nhiên để tránh bị phát hiện bot."""
    time.sleep(base + random.uniform(0.5, 1.5))


def login(page) -> bool:
    """Đăng nhập Facebook."""
    print("[*] Đang đăng nhập...")
    page.goto("https://www.facebook.com/login", wait_until="domcontentloaded")
    human_delay(1)

    page.fill("#email", FB_EMAIL)
    page.fill("#pass", FB_PASSWORD)
    page.click("[name='login']")

    try:
        page.wait_for_url("https://www.facebook.com/", timeout=15000)
        print("[+] Đăng nhập thành công.")
        return True
    except PlaywrightTimeoutError:
        # Có thể cần xác minh 2FA
        print("[!] Cần xác minh thủ công (2FA / CAPTCHA). Hãy hoàn tất trong 60 giây...")
        try:
            page.wait_for_url("https://www.facebook.com/", timeout=60000)
            print("[+] Xác minh thành công.")
            return True
        except PlaywrightTimeoutError:
            print("[-] Đăng nhập thất bại.")
            return False


def open_activity_log_year(page, year: int) -> None:
    """Mở Activity Log và lọc theo năm."""
    url = f"{ACTIVITY_LOG_URL}?category_key=NONE&year={year}"
    print(f"[*] Mở Activity Log năm {year}...")
    page.goto(url, wait_until="domcontentloaded")
    human_delay(2)


def scroll_and_collect_items(page, selector: str, max_items: int = 500) -> list:
    """Cuộn trang và thu thập các phần tử."""
    items = []
    last_count = 0
    no_change_streak = 0

    while len(items) < max_items:
        elements = page.query_selector_all(selector)
        if len(elements) == last_count:
            no_change_streak += 1
            if no_change_streak >= 3:
                break
        else:
            no_change_streak = 0
            last_count = len(elements)
            items = elements

        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        human_delay(1.5)

    return items


def click_three_dot_menu(page, item_element) -> bool:
    """Click vào menu 3 chấm của một bài đăng."""
    try:
        # Hover vào item để hiện nút menu
        item_element.hover()
        human_delay(0.5)

        # Tìm nút 3 chấm (aria-haspopup hoặc aria-label chứa từ khoá)
        btn = item_element.query_selector("[aria-haspopup='menu']")
        if not btn:
            btn = item_element.query_selector("[data-visualcompletion='ignore-dynamic']")
        if not btn:
            return False

        btn.click()
        human_delay(0.8)
        return True
    except Exception:
        return False


def delete_post(page) -> bool:
    """Chọn 'Xoá' từ menu đang mở."""
    try:
        # Tìm option 'Delete' hoặc 'Xoá'
        delete_option = page.query_selector_all("[role='menuitem']")
        for opt in delete_option:
            text = opt.inner_text().strip().lower()
            if "xoá" in text or "delete" in text or "remove" in text:
                opt.click()
                human_delay(1)

                # Xác nhận xoá nếu có dialog
                confirm_btn = page.query_selector("[data-testid='dialog-confirm-button']")
                if not confirm_btn:
                    # Tìm nút xác nhận theo text
                    for btn in page.query_selector_all("button"):
                        t = btn.inner_text().strip().lower()
                        if "xác nhận" in t or "confirm" in t or "xoá" in t or "delete" in t:
                            confirm_btn = btn
                            break

                if confirm_btn:
                    confirm_btn.click()
                    human_delay(1)

                print("  [+] Đã xoá.")
                return True

        print("  [!] Không tìm thấy tùy chọn Xoá.")
        return False
    except Exception as e:
        print(f"  [!] Lỗi khi xoá: {e}")
        return False


def set_private(page) -> bool:
    """Chọn 'Chỉnh sửa quyền riêng tư' -> 'Chỉ mình tôi'."""
    try:
        options = page.query_selector_all("[role='menuitem']")
        for opt in options:
            text = opt.inner_text().strip().lower()
            if "privacy" in text or "quyền riêng tư" in text or "audience" in text:
                opt.click()
                human_delay(1)
                break
        else:
            # Thử menu "Edit audience" / "Edit privacy"
            for opt in options:
                text = opt.inner_text().strip().lower()
                if "edit" in text or "chỉnh sửa" in text:
                    opt.click()
                    human_delay(1)
                    break
            else:
                return False

        # Chọn "Only me" / "Chỉ mình tôi"
        for btn in page.query_selector_all("[role='radio'], [role='option'], div[tabindex]"):
            text = btn.inner_text().strip().lower()
            if "only me" in text or "chỉ mình tôi" in text:
                btn.click()
                human_delay(0.8)
                break

        # Lưu thay đổi
        for btn in page.query_selector_all("button"):
            text = btn.inner_text().strip().lower()
            if "done" in text or "save" in text or "xong" in text or "lưu" in text:
                btn.click()
                human_delay(1)
                break

        print("  [+] Đã đặt riêng tư.")
        return True
    except Exception as e:
        print(f"  [!] Lỗi khi đổi quyền riêng tư: {e}")
        return False


def process_activity_log(page, year: int) -> None:
    """
    Duyệt Activity Log:
    - Bài SHARE  -> Xoá
    - Bài tự viết -> Đặt riêng tư
    """
    open_activity_log_year(page, year)

    deleted_count  = 0
    private_count  = 0
    skipped_count  = 0
    processed_ids  = set()

    print(f"\n[*] Bắt đầu xử lý bài đăng năm {year}...\n")

    while True:
        # Lấy tất cả dòng trong activity log
        rows = page.query_selector_all("[data-testid='activitylog_item'], [class*='activitylog']")
        if not rows:
            # Fallback: lấy các article/div chứa bài đăng
            rows = page.query_selector_all("article, [role='article']")

        if not rows:
            print("[!] Không tìm thấy bài đăng nào. Có thể giao diện Facebook đã thay đổi.")
            break

        found_new = False

        for row in rows:
            row_id = id(row)
            if row_id in processed_ids:
                continue

            found_new = True
            processed_ids.add(row_id)

            try:
                text = row.inner_text()
            except Exception:
                continue

            text_lower = text.lower()
            is_share = (
                "đã chia sẻ" in text_lower
                or "shared" in text_lower
                or "chia sẻ" in text_lower
            )

            if is_share:
                print(f"  [SHARE] Đang xoá: {text[:60].strip()}...")
                if click_three_dot_menu(page, row):
                    if delete_post(page):
                        deleted_count += 1
                    else:
                        skipped_count += 1
                else:
                    skipped_count += 1
                human_delay()
            else:
                print(f"  [POST]  Đang đặt riêng tư: {text[:60].strip()}...")
                if click_three_dot_menu(page, row):
                    if set_private(page):
                        private_count += 1
                    else:
                        skipped_count += 1
                else:
                    skipped_count += 1
                human_delay()

        if not found_new:
            # Thử cuộn xuống để load thêm
            prev_height = page.evaluate("document.body.scrollHeight")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            human_delay(2)
            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == prev_height:
                print("[*] Đã xử lý hết bài đăng.")
                break

    print(f"\n{'='*50}")
    print(f"KẾT QUẢ:")
    print(f"  Đã xoá (bài share):        {deleted_count}")
    print(f"  Đã đặt riêng tư (tự viết): {private_count}")
    print(f"  Bỏ qua (lỗi):             {skipped_count}")
    print(f"{'='*50}\n")


def main():
    if not FB_EMAIL or not FB_PASSWORD:
        print("[-] Chưa cấu hình FB_EMAIL và FB_PASSWORD trong file .env")
        print("    Hãy sao chép .env.example thành .env và điền thông tin.")
        sys.exit(1)

    print("=" * 50)
    print("Facebook Post Cleanup Tool")
    print(f"Năm xử lý: {TARGET_YEAR}")
    print(f"Headless:  {HEADLESS}")
    print("=" * 50)
    print()
    print("[!] LƯU Ý: Tool sẽ THỰC SỰ XOÁ bài share và ĐỔI QUYỀN RIÊNG TƯ bài tự viết.")
    print("    Hãy chắc chắn bạn đã backup dữ liệu Facebook trước (Settings > Your Facebook Information > Download Your Information).")
    print()

    confirm = input("Nhập 'yes' để tiếp tục: ").strip().lower()
    if confirm != "yes":
        print("Đã huỷ.")
        sys.exit(0)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=HEADLESS,
            args=["--disable-blink-features=AutomationControlled"],
        )
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            locale="vi-VN",
        )
        page = context.new_page()

        try:
            if not login(page):
                sys.exit(1)

            process_activity_log(page, TARGET_YEAR)

        except KeyboardInterrupt:
            print("\n[!] Đã dừng bởi người dùng.")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
