# Meeting Notes: Project Topic Selection

**Date:** Week 1 - Project Kickoff  
**Meeting Type:** Project Topic Selection  
**Attendees:** All Team Members (Group 04)

## Participants
- Mai Chiến Hữu (20205230) - Project Lead
- Nguyễn Bá Tùng Lâm (20226053)
- Trần Đức Huy (20194780)
- Đặng Đức Dương (20225965)
- Mai Tuấn Kiên (20226051)
- Lê Vương Khánh (20204989)
- Trần Chí Thành (20194845)

## Meeting Objective
To select an appropriate project topic for the Software Management mini-project that aligns with course requirements and team capabilities.

## Discussion Summary

### Topics Considered
The team discussed several potential project ideas focusing on software management and agile methodologies:

1. **Agile Project Management System (Selected)**
   - Full-stack application for managing Scrum-based projects
   - Support for complete project lifecycle management
   - Integration of key Agile concepts: Projects, Sprints, Epics, Work Items
   - Resource and cost tracking capabilities

2. Other considerations (discussed but not pursued)
   - Simple task tracking application
   - Issue tracking system
   - Time management tool

### Rationale for Selection

The team chose the **Agile Project Management System (Scrum PM)** for the following reasons:

1. **Alignment with Course Content**: Directly applies software management principles and Agile methodologies covered in the course
2. **Practical Relevance**: Addresses real-world needs in software project management
3. **Technical Challenge**: Provides opportunity to work with modern full-stack technologies
4. **Comprehensive Scope**: Allows demonstration of project planning, execution, and monitoring capabilities
5. **Team Learning**: Enables hands-on experience with Scrum practices while building a Scrum tool
6. **Scalability**: Project can be expanded with additional features if time permits

### Key Features Agreed Upon

The team agreed to implement the following core features:

1. **Project Portfolio Management**
   - Create and manage multiple projects
   - Track project status (Planning, Active, Archived)
   - Dashboard with project statistics

2. **Epic & Backlog Management**
   - Define high-level features as Epics
   - Break down Epics into Work Items
   - Classify work items by type (Story, Bug, Task)
   - Priority management (Low, Medium, High, Critical)

3. **Sprint Planning & Execution**
   - Create and manage sprints
   - Assign work items to sprints
   - Track sprint progress and status

4. **Resource Management**
   - Maintain people/team member records
   - Assign resources to Epics or Work Items
   - Track allocation and workload

5. **Cost Management**
   - Define cost items
   - Assign costs to Epics or Work Items
   - Aggregate estimated costs by project/sprint

6. **Timeline & Reporting**
   - Visual timeline of sprint dates
   - Project dashboards with key metrics

### Technical Stack Decision

The team agreed on the following technology stack:

**Backend:**
- Java 21 with Spring Boot 3
- Spring Data JPA with Hibernate
- H2 database for development (with MySQL option for production)
- RESTful API architecture

**Frontend:**
- React 18 with TypeScript
- Vite as build tool
- TailwindCSS with shadcn/ui components
- React Router for navigation
- Axios for API calls
- TanStack Query for data management

**Rationale:** This stack leverages modern, industry-standard technologies that team members are familiar with or want to learn, ensuring both productivity and skill development.

### Project Timeline

The team established a 10-week timeline:
- Week 1: Requirements, setup, environment configuration
- Weeks 2-4: Core entities and basic CRUD operations
- Weeks 5-7: Advanced features (Sprint planning, Resource/Cost management)
- Week 8: Timeline, dashboards, and aggregations
- Week 9: Quality assurance and refinement
- Week 10: UAT, documentation, and final demo

### Agile Methodology Adoption

The team committed to using Scrum methodology for the project itself:
- 2-week sprints
- Regular sprint planning, daily standups, reviews, and retrospectives
- Maintained Product Backlog and Sprint Backlog
- Definition of Ready and Definition of Done for all work items

## Decision

**UNANIMOUS AGREEMENT:** The team unanimously agreed to proceed with the **Scrum PM Application** (Agile Project Management System) as the project topic.

## Action Items

- [x] Document project description and requirements - *Completed in Project_Description.md*
- [x] Set up project repository structure - *Completed*
- [x] Initialize backend project (Spring Boot) - *Completed*
- [x] Initialize frontend project (React + TypeScript) - *Completed*
- [x] Define entity models and relationships - *Completed*
- [x] Create comprehensive README - *Completed*

## Next Steps

1. Begin Week 2 activities: Domain modeling and database schema design
2. Implement core entity classes (Project, Epic, Sprint, Work Item, Person, Cost)
3. Set up API skeleton and basic CRUD endpoints
4. Start frontend routing and layout structure

## References

- [Project Description](./Project_Description.md) - Comprehensive project overview and requirements
- [README](./README.md) - Technical documentation and getting started guide
- Repository: https://github.com/huumai1903/MiniProject-SoftwareMangement

---

**Meeting concluded with clear direction and team alignment on the project topic and implementation approach.**
