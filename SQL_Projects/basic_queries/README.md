# Basic SQL Queries

This folder contains a collection of SQL queries demonstrating analytical and data processing skills.

## Queries Included

1. **Second Highest Salary per Department**
   - Finds the second highest salary in each department using DENSE_RANK() and CTEs.
   - Tables: Employees, Departments

2. **Customers with >3 Orders in a Month**
   - Returns customers who placed more than 3 orders in any calendar month.
   - Table: Orders

3. **Employees without a Manager**
   - Finds employees who never reported to a manager.
   - Table: Employees

4. **Employee & Manager Relationships**
   - Self-joins to find each employee with their manager and employees sharing the same manager.

5. **Hierarchical Categories**
   - Finds parent → child relationships in the same table using self-join.
   - Table: Categories

6. **First Purchase Date & Total Amount**
   - Calculates first purchase date per user and total spent after that date.
   - Table: Purchases

7. **Rolling Averages & Sums**
   - 7-day rolling average and other moving sums of sales.
   - Table: Sales

8. **Days Between First Visit and First Purchase**
   - Calculates days between first visit and first purchase per user.
   - Tables: Visits, Purchases

## How to Run
- Load the sample tables into your SQL database.
- Copy queries from `basic_queries.sql` and run them in your SQL editor.

## Sample Data
- Sample tables for Employees, Departments, Orders, Purchases, Sales, Visits, and Categories are provided in `sample_data.sql`.
