# Facebook Post Cleanup Tool

Tự động dọn dẹp bài đăng Facebook theo năm:
- **Bài share** → Xoá hoàn toàn
- **Bài tự viết** → Chuyển sang "Chỉ mình tôi"

## Cài đặt

```bash
pip install -r requirements.txt
playwright install chromium
```

## Cấu hình

```bash
cp .env.example .env
# Chỉnh sửa .env với email/mật khẩu Facebook của bạn
```

## Chạy

```bash
python fb_cleanup.py
```

## Lưu ý quan trọng

1. **Backup trước** — Vào *Settings → Your Facebook Information → Download Your Information* để tải về bản sao dữ liệu trước khi xoá.
2. **Headless = false** (mặc định) — Tool hiển thị trình duyệt để bạn theo dõi và xử lý 2FA/CAPTCHA nếu cần.
3. **Rate limit** — Nếu Facebook chặn, tăng `DELAY_BETWEEN_ACTIONS` trong `.env` lên 3–5 giây.
4. **Giao diện thay đổi** — Facebook thường xuyên cập nhật UI. Nếu script không nhận dạng được nút, mở issue hoặc chạy với `HEADLESS=false` để debug.
5. **2FA** — Nếu tài khoản bật xác minh 2 bước, script sẽ chờ 60 giây để bạn nhập mã thủ công.
