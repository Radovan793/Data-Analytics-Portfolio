/************************************************************
 * Basic SQL Queries
 * Python-SQL-Mini-Projects / SQL_Projects / basic_queries
 *
 * This file contains a collection of SQL queries demonstrating
 * analytical and data processing skills using window functions,
 * CTEs, self-joins, and basic aggregation techniques.
 ************************************************************/

/************************************************************
 * 1. Find the second highest salary in each department
 ************************************************************/
-- Tables: Employees(emp_id, name, salary, department_id)
--         Departments(department_id, department_name)

WITH second_highest_salary AS (
    SELECT d.*,
           DENSE_RANK() OVER (PARTITION BY d.department_id ORDER BY e.salary DESC) AS salary_rank
    FROM Departments d
    JOIN Employees e 
      ON d.department_id = e.department_id
)
SELECT d.department_id, 
       d.department_name, 
       e.salary, 
       salary_rank
FROM second_highest_salary
WHERE salary_rank = 2;


/************************************************************
 * 2. Identify customers who placed more than 3 orders in a month
 ************************************************************/
-- Tables: Orders(order_id, customer_id, order_date)
SELECT customer_id,
       YEAR(order_date) AS order_year,
       MONTH(order_date) AS order_month,
       COUNT(order_id) AS order_count
FROM Orders
GROUP BY customer_id, YEAR(order_date), MONTH(order_date)
HAVING COUNT(order_id) > 3
ORDER BY order_year, order_month;


/************************************************************
 * 3. Get employees who never reported to a manager
 ************************************************************/
-- Table: Employees(emp_id, name, manager_id)
SELECT emp_id, name
FROM Employees
WHERE manager_id IS NULL;


/************************************************************
 * 4. Employee & Manager Relationships
 ************************************************************/
-- 4a. Each employee with their manager
SELECT e.emp_id AS employee_id,
       e.name AS employee_name,
       m.name AS manager_name
FROM Employees e
LEFT JOIN Employees m
  ON e.manager_id = m.emp_id;

-- 4b. Employees sharing the same manager
SELECT e1.name AS employee1,
       e2.name AS employee2,
       e1.manager_id
FROM Employees e1
JOIN Employees e2
  ON e1.manager_id = e2.manager_id
WHERE e1.emp_id < e2.emp_id;


/************************************************************
 * 5. Hierarchical categories or folders
 ************************************************************/
-- Table: Categories(category_id, category_name, parent_id)
SELECT c1.category_name AS parent,
       c2.category_name AS child
FROM Categories c1
JOIN Categories c2
  ON c1.category_id = c2.parent_id;


/************************************************************
 * 6. First purchase date and total amount spent after
 ************************************************************/
-- Table: Purchases(purchase_id, user_id, purchase_date, amount)
WITH first_purchase AS (
    SELECT user_id, 
           MIN(purchase_date) AS first_purchase_date
    FROM Purchases
    GROUP BY user_id
),
total_amount_spent AS (
    SELECT fp.user_id, 
           fp.first_purchase_date,
           COALESCE(SUM(p.amount), 0) AS total_spent
    FROM first_purchase fp
    LEFT JOIN Purchases p
      ON fp.user_id = p.user_id
     AND p.purchase_date > fp.first_purchase_date
    GROUP BY fp.user_id, fp.first_purchase_date
)
SELECT *
FROM total_amount_spent
ORDER BY user_id;


/************************************************************
 * 7. Rolling averages & sums
 ************************************************************/
-- Table: Sales(sale_id, sale_date, amount)

-- 7a. 7-day rolling average of sales
SELECT sale_date,
       AVG(amount) OVER (
         ORDER BY sale_date
         ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
       ) AS rolling_avg
FROM Sales
ORDER BY sale_date;

-- 7b. Moving sum examples
SELECT order_id,
       sale_amount,
       SUM(sale_amount) OVER (
         ORDER BY order_date
         ROWS BETWEEN CURRENT ROW AND 3 FOLLOWING
       ) AS moving_sum
FROM sales;

SELECT order_id,
       sale_amount,
       SUM(sale_amount) OVER (
         ORDER BY order_date
         ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING
       ) AS rolling_sum
FROM sales;


/************************************************************
 * 8. Days between first visit and first purchase
 ************************************************************/
-- Tables: Visits(user_id, visit_date), Purchases(user_id, purchase_date)
WITH first_visit AS (
    SELECT user_id,
           MIN(visit_date) AS first_visit_date
    FROM Visits
    GROUP BY user_id
),
first_purchase AS (
    SELECT user_id,
           MIN(purchase_date) AS first_purchase_date
    FROM Purchases
    GROUP BY user_id
)
SELECT v.user_id,
       DATEDIFF(p.first_purchase_date, v.first_visit_date) AS days_between
FROM first_visit v
JOIN first_purchase p
  ON v.user_id = p.user_id;
