Database Schema

Employees Table
| Column | Type    | Constraints      |
| ------ | ------- | ---------------- |
| id     | INTEGER | Primary Key      |
| name   | VARCHAR | Not Null         |
| role   | VARCHAR | Not Null         |
| email  | VARCHAR | Unique, Not Null |

Tasks Table
| Column      | Type    | Constraints                           |
| ----------- | ------- | ------------------------------------- |
| id          | INTEGER | Primary Key                           |
| title       | VARCHAR | Not Null                              |
| description | VARCHAR | Nullable                              |
| status      | VARCHAR | Default: "Pending"                    |
| employee_id | INTEGER | Foreign Key → employees.id (Nullable) |
