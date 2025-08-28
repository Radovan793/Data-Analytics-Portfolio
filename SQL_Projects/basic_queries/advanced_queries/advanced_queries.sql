-- 1. Find duplicate values in 'users' table

SELECT * 
FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY user_name ORDER BY user_id) AS rn
    FROM users
) AS t
WHERE rn <> 1;


-- 2. Fetch top 3 employees in each department by highest salary

SELECT * 
FROM (
    SELECT *, RANK() OVER(PARTITION BY dept_name ORDER BY salary DESC) AS rnk
    FROM employee
) AS ranked_employees
WHERE rnk < 4;


-- 3. Find cities with 3+ consecutive days of temperature below 0°C

SELECT DISTINCT city, day, temperature
FROM (
    SELECT city, day, temperature,
        CASE 
            WHEN temperature < 0 
                 AND LAG(temperature, 1) OVER(PARTITION BY city ORDER BY day) < 0
                 AND LAG(temperature, 2) OVER(PARTITION BY city ORDER BY day) < 0
            THEN 1
            ELSE 0 
        END AS cold_streak
    FROM weather
) AS x
WHERE cold_streak = 1 AND city = 'London'
ORDER BY city, day;


-- 4. Find the second highest salary in each department

WITH second_highest_salary AS (
    SELECT d.department_id, d.department_name, e.salary,
           DENSE_RANK() OVER(PARTITION BY d.department_id ORDER BY e.salary DESC) AS highest_salary
    FROM Departments d
    JOIN Employees e ON d.department_id = e.department_id
)
SELECT department_id, department_name, salary
FROM second_highest_salary
WHERE highest_salary = 2;
