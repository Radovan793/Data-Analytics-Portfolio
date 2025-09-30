# Advanced SQL Queries

This folder contains a collection of advanced SQL queries demonstrating analytical and data processing skills.  
Each query is focused on solving a specific real-world problem using window functions, CTEs, and ranking techniques.

---

## Queries Included

1. **Find Duplicate Records**  
   - Detects duplicate entries in a table based on a unique key.  
   - Demonstrates use of `ROW_NUMBER()` window function.

2. **Top 3 Employees by Salary per Department**  
   - Fetches top earners in each department using `RANK()`.  
   - Useful for HR analytics and performance reporting.

3. **Cities with 3+ Consecutive Cold Days**  
   - Identifies cities where temperatures remained below 0°C for three or more consecutive days.  
   - Demonstrates use of `LAG()` and conditional logic.

4. **Second Highest Salary in Each Department**  
   - Finds the second highest salary per department using `DENSE_RANK()` and CTEs.  
   - Example for ranking and departmental salary analysis.

5. **Consecutive cold weather streaks**  
   - Find cities with 3 or more + consequitive days of cold weather temperature below 0 Degress C.
   - Demonstrates use of CASE WHEN THEN with window functions `LEAD() and LAG()`and CTEs.  

---

## How to Run
1. Load the sample tables (`users`, `employee`, `Departments`, `weather`) in your SQL database.  
2. Copy queries from `advanced_queries.sql` and execute them in your SQL editor.

### Sample Data
A sample dataset is included in [sample_data.sql](sample_data.sql).  
Load it into your SQL environment before running the queries.
---

## Skills Demonstrated
- **Window Functions**: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`  
- **Common Table Expressions (CTEs)**  
- **Conditional Aggregation**  
- **Data Cleaning & Analysis**





# Advanced SQL Queries – Part 2

This file contains additional **advanced SQL queries**, extending the examples from `advanced_queries.sql`.  
Focus is on analytical tasks, aggregations, and multi-step data processing using **CTEs, scalar subqueries, and combined calculations**.

---

## Queries Included

### Total Sales per Client vs Overall Average
- Calculates total sales for each client.
- Compares each client’s total with the overall average.
- Demonstrates scalar subqueries and aggregation logic.

### Chaining CTEs
- Computes per-client totals in one CTE.
- Computes overall average totals in a second CTE.
- Combines results using `CROSS JOIN` for comparison.

### Invoices Above Client Average
- Selects invoices exceeding the client-specific average invoice total.
- Demonstrates correlated subqueries for per-client calculations.

### Employees with Salary Above Office Average
- Identifies employees earning more than the average in their office.
- Uses correlated subqueries to compare rows within the same department/office.

### Products Never Ordered
- Finds products with no associated orders.
- Demonstrates `NOT EXISTS` for safe exclusion even with potential NULLs.

---

## How to Run
1. Load the sample tables (`clients`, `invoices`, `employees`, `products`, `order_items`) in your SQL database.
2. Copy queries from `advanced_queries2.sql` and execute them in your SQL editor.

---

## Sample Data
Use `sample_data.sql` to populate tables if needed.  
Minimal rows are sufficient to test query logic.

---

## Skills Demonstrated
- Common Table Expressions (CTEs)  
- Correlated subqueries  
- Scalar subqueries in `SELECT` clauses  
- Aggregation and comparisons  
- Safe usage of `NOT EXISTS` and `IN`  

---

## Next Steps
More queries will be added, including:  
- Complex joins and aggregations  
- Advanced date/time analytics  
- Performance optimization examples
