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

---

## Next Steps
More queries will be added, including:  
- Complex joins and aggregations  
- Advanced date/time analytics  
- Performance optimization examples
