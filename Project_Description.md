PROJECT DESCRIPTION - GROUP 04  
SCRUM PM APPLICATION

PROJECT OVERVIEW  
Scrum PM is a full-stack web app for managing the software project lifecycle with Scrum. It supports project portfolio, Epic/Sprint planning, backlog execution, resource and cost tracking. Users can create projects, add Epics and Work Items (story/bug/task), assign them to sprints, allocate people and costs, and monitor progress through timelines and project dashboards.

KEY FEATURE & USER ROLES  
- Portfolio & dashboard: project list with status filters, epic count, team size, and estimated cost; quick access into each project.  
- Epic & backlog: create/update Epics and Work Items; classify by type (story/bug/task), priority, and status; backlog table filters by sprint or unassigned items.  
- Sprint planning & execution: create/edit sprints, view work items per sprint, track DONE/IN_PROGRESS/TO_DO and execution progress.  
- Resource management: organization-wide People list; assign members to Epics/Work Items, view allocation by sprint and workload.  
- Cost management: define Cost items, assign costs to Epics/Work Items, aggregate estimated cost by project and sprint.  
- Timeline: overview of sprint dates and key project activities.

User Roles (aligned with current features):  
- Project Manager/Product Owner: create/update projects, epics, work items; plan sprints; allocate people/costs; track progress, timeline, and total cost.  
- Team Member: view assigned backlog/sprint items, update work item status, report progress.  
- Admin/PMO: manage shared People and Cost catalogs, control project configuration, support consolidated reporting.

TECHNICAL STACK  
- Backend: Java 21, Spring Boot 3 (Web/MVC, Spring Data JPA, Hibernate), manual DTO mapping; RESTful API.  
- Database: H2 (dev, file-based). MySQL can be configured for production deployment.  
- Build/Tooling: Maven; Lombok for reduced boilerplate; JPA schema auto-generation.  
- Frontend: React 18 + TypeScript, Vite, TailwindCSS + shadcn/ui (Radix), React Router, Axios, TanStack Query for data fetching/caching.  
- Integration: frontend calls backend via REST; clear layering between services (API clients) and components/views (Epics, Sprint, Backlog, Resource, Cost, Timeline).

PROJECT TIMELINE (10 WEEKS)  
- Week 1: Kickoff, requirements, scope, success criteria, team setup, environment setup (backend + frontend).  
- Week 2: Domain modeling, database schema, core entities (Project, Epic, Sprint, Work Item, Person, Cost), API skeleton.  
- Week 3: Project & Epic CRUD, basic backlog API/UI, routing & layout on frontend.  
- Week 4: Work Item CRUD, priority/status/type handling, backlog view with filters.  
- Week 5: Sprint planning/execution flows (create/edit sprints, assign items), sprint board UI.  
- Week 6: Resource module (People list, assignments to Epic/Work Item, workload view).  
- Week 7: Cost module (cost items, cost assignments, estimated totals per project/sprint).  
- Week 8: Timeline view, dashboards, aggregated stats (epic count, team size, cost).  
- Week 9: Quality hardening (validation, error handling, API/UX polish), risk mitigation actions.  
- Week 10: UAT, performance checks, documentation, handover/demo.

PROCESS & PRACTICES  
- Scrum: 2-week sprints; artifacts (Product Backlog, Sprint Backlog, Increment); ceremonies (Sprint Planning, Daily Scrum, Review, Retrospective).  
- Task breakdown: Epics → Stories/Tasks/Bugs; Definition of Ready/Done maintained in backlog views.  
- Assignment: people assigned to Epic/Work Item; visibility via Resource and Backlog views.  
- Quality management: API/DTO validation, status/priority constraints, UI error states; planned manual regression and basic unit tests; backlog for defects; Demo/UAT in Week 10.  
- Risk management: tracked risks for scope creep, schedule slip, integration gaps, data consistency; mitigations include weekly risk review, prioritized backlog, incremental releases, and fallback to H2 for dev with MySQL plan for prod.  
- Communication & collaboration: project dashboard for shared visibility; sprint board/backlog for alignment; async updates via status fields; ceremonies cadence (planning/review/retro) to surface blockers; PM/PO owns priorities, team updates status daily. 
