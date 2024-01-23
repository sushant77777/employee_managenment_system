# Employee Management System

This is a minimal Employee Management System developed using Django. The system comprises three main modules: Employee Management, Department Management, and Employee Salary Management.

## Features

### Employee Management
- Admin page for adding, updating, and deleting employees.
- Employee attributes include Name, Email, Address, Designation, Reporting Manager, and Department.

### Department Management
- Admin page for adding, updating, and deleting departments.
- Hierarchical reporting page to display employee hierarchy within each department.

### Employee Salary Management
- Admin page for adding, updating, and deleting employee salary entries with date ranges.
- Reporting page to view department-wise salary costs within a specified date range.

## Employee Designations
- Employees can have designations as Associate, TL (Team Lead), or Manager.

## Reporting Hierarchy Example
```
Steve Jobs (Manager)
|
|-- Steve Wozniak (TL Engineering)
|   |
|   |-- Emp1
|   |-- Emp2
|
|-- Tim Cook (TL Apple Watch)
|   |
|   |-- Emp3
|
|-- Andy Hertz (TL iPad)
    |
    |-- Emp4
    |-- Emp5
```

## Department Salary Costs Example (Date Range: 1 Jan to 1 November)
- HR: $100,000
- Python Team: $200,000
- PHP Team: $150,000
- IT Team: $100,000

## Tech Stack
- Python
- Django
- Database: MySQL/MariaDB/Mongo/SQLite
- Additional libraries as per requirements

## Setup Instructions
1. Clone the repository.
2. Install the required dependencies.
3. Configure the database settings.
4. Run migrations to set up the database schema.
5. Launch the Django development server.

## Usage
1. Access the admin pages to manage employees, departments, and salary entries.
2. Explore the reporting pages to visualize employee hierarchy and department-wise salary costs.

## Notes
- Django Admin customization is implemented for easy management.
- Reporting pages use views with JavaScript (JQuery or DataTables).

Feel free to reach out for any clarifications or assistance during the setup to
sushant suryavanshi at sushantsuryavanshi77777@gmail.com 
**Estimated Completion Time:** 1 week
