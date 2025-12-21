# Agile Project Management System

This is a full-stack Agile project management system backend built with **Spring Boot**, utilizing **JPA/Hibernate** for ORM and automatic database schema generation. It supports key concepts in Agile workflows such as **Projects**, **Sprints**, **Epics**, **Work Items**, and associated **Personnel** and **Costs**.

## Team members
- Mai Chiến Hữu - 20205230 - huumai1903 - init code backend + code cost services + partially code frontend (Project Lead)
- Nguyễn Bá Tùng Lâm - 20226053 - hust.20226053@gmail.com - Code Epic Managment function
- Trần Đức Huy - 20194780 - cudhuy - init code frontend + code services to connect backend api
- Đặng Đức Dương - 20225965 - dangducduong1412 - Code sprint managemnet function
- Mai Tuấn Kiên - 20226051 - KienMai04 - Code person managemnent function
- Lê Vương Khánh - 20204989 - KhanhLV146 - Code project management function
- Trần Chí Thành - 20194845 - TrnChThnh1301 - Code workitem management function

## Features

- Create and manage multiple projects
- Define epics and break them down into work items
- Organize work items into sprints with execution and review cycle
- Assign personnel and allocate costs to specific work items or epics
- Automatically generate relational database schema from JPA models
- RESTful APIs for integration with a frontend (React)

## Entities & Relationships

### Entities

- `Project`: Represents a project lifecycle
- `Sprint`: A time-boxed development cycle
- `Epic`: A high-level feature or goal
- `WorkItem`: A task or requirement (story, bug, etc.)
- `Person`: Team member
- `Cost`: Expense item (personnel, material, etc.)
- `PersonAssignment`: Links a person to either an epic or a work item with allocated hours (mutually exclusive).
- `CostAssignment`: Links a cost record to either an epic or a work item (mutually exclusive).

### Relationships & Rules

- `Project` owns many `Sprint`, `Epic`, and `WorkItem` records (cascade creates/updates).
- `Sprint` belongs to a project and manages its `WorkItem` list. Helper methods enforce valid status transitions and move incomplete items back to backlog or into another sprint on completion.
- `Epic` belongs to a project and groups related work items plus any people or cost assignments attached to that epic.
- `WorkItem` belongs to a project and can optionally belong to a sprint and/or epic. Location (`BACKLOG` | `SPRINT` | `COMPLETED`) is validated against status and sprint presence to keep data consistent.
- `Person` is associated through `PersonAssignment`; exactly one of epic/work item must be set, and hours cannot be negative.
- `Cost` is associated through `CostAssignment`; exactly one of epic/work item must be set, and cost amounts cannot be negative.

### Status & Enum Values

- `ProjectStatus`: `PLANNING`, `ACTIVE`, `ARCHIVED`
- `SprintStatus`: `NOT_STARTED`, `ACTIVE`, `COMPLETED`
- `WorkItemStatus`: `TODO`, `IN_PROGRESS`, `DONE`
- `WorkItemType`: `TASK`, `STORY`, `BUG`
- `WorkItemPriority`: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`
- `WorkItemLocation`: `BACKLOG`, `SPRINT`, `COMPLETED`

## Tech Stack

- **Backend**: Java 21, Spring Boot 3.2.3 (Web, Spring Data JPA, Hibernate), Lombok
- **Database**: H2 file-based for development (`./data/project-db`); ready for MySQL in production
- **Frontend**: React 18 + TypeScript, Vite, TailwindCSS with shadcn/ui, React Router, Axios, TanStack Query
- **Build/Tooling**: Maven (backend with `mvnw` wrapper), Node 18+ with npm for the frontend

## Getting Started

### Prerequisites

- Java 21+
- Maven (or use the provided `mvnw` script)
- Node.js 18+ and npm
- IDE (e.g. IntelliJ IDEA, VSCode)

### Clone the repository

```bash
git clone https://github.com/huumai1903/MiniProject-SoftwareMangement.git
cd MiniProject-SoftwareMangement
```

### Backend (Spring Boot)

```bash
cd project-management-be
# Optional: activate dev profile to load sample seed data
./mvnw spring-boot:run -Dspring-boot.run.profiles=dev
```

- API base URL: `http://localhost:8080/api`
- H2 console (dev): `http://localhost:8080/h2-console` (JDBC URL `jdbc:h2:file:./data/project-db`, username `sa`, blank password)

### Frontend (React + Vite)

```bash
cd project-management-fe
npm install
npm run dev -- --port 5173
```

- The frontend expects the backend at `http://localhost:8080/api` (see `src/lib/api.ts`). Start the backend first, then open the Vite dev server (default `http://localhost:5173` or your chosen port).
