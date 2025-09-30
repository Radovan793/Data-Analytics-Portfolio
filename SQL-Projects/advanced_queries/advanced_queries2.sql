-- Clients with at least 2 invoices

SELECT c.* ,i.invoice_id 
FROM clients c
JOIN invoices i
WHERE i.client_id IN (
    SELECT client_id
    FROM invoices
    GROUP BY client_id
    HAVING COUNT(*) >= 2
);

-- Correlated subquery: get employees with salary > avg salary in their office

SELECT *
FROM employees e
WHERE salary > (
    SELECT AVG(c.salary)
    FROM employees c
    WHERE e.office_id = c.office_id
);

-- Invoices greater than the client's average

SELECT *
FROM invoices i
WHERE i.invoice_total > (
    SELECT AVG(u.payment_total)
    FROM invoices u
    WHERE u.client_id = i.client_id
);

-- Subqueries in SELECT clause

SELECT invoice_id, 
       invoice_total,
       (SELECT AVG(invoice_total) FROM invoices) AS invoice_average,
       invoice_total - (SELECT AVG(invoice_total) FROM invoices) AS difference
FROM invoices;

-- Same query using a CTE (MySQL 8.0+)

WITH avg_val AS (
    SELECT AVG(invoice_total) AS invoice_average
    FROM invoices
)
SELECT i.invoice_id,
       i.invoice_total,
       a.invoice_average,
       i.invoice_total - a.invoice_average AS difference
FROM invoices i
CROSS JOIN avg_val a;

-- Scalar subqueries: total sales per client, overall avg, and difference

SELECT 
    c.client_id, 
    c.name,
    (SELECT SUM(invoice_total)
     FROM invoices 
     WHERE client_id = c.client_id) AS total_sales,
    (SELECT AVG(invoice_total) 
     FROM invoices) AS average,
    ((SELECT SUM(invoice_total)
      FROM invoices 
      WHERE client_id = c.client_id)
     - 
     (SELECT AVG(invoice_total) 
      FROM invoices)) AS difference
FROM clients c;

-- Cleaner version with CTEs

WITH client_sales AS (
    SELECT 
        c.client_id,
        c.name,
        SUM(i.invoice_total) AS total_sales
    FROM clients c
    LEFT JOIN invoices i 
        ON i.client_id = c.client_id
    GROUP BY c.client_id, c.name
),
overall_avg AS (
    SELECT AVG(invoice_total) AS average 
    FROM invoices
)
SELECT 
    cs.client_id,
    cs.name,
    cs.total_sales,
    oa.average,
    cs.total_sales - oa.average AS difference
FROM client_sales cs
CROSS JOIN overall_avg oa;

-- Chaining CTEs example

WITH client_totals AS (
    SELECT client_id, SUM(invoice_total) AS total_sales
    FROM invoices
    GROUP BY client_id
),
overall_avg AS (
    SELECT AVG(total_sales) AS average
    FROM client_totals
)
SELECT 
    c.client_id,
    c.name,
    ct.total_sales,
    oa.average,
    ct.total_sales - oa.average AS difference
FROM clients c
LEFT JOIN client_totals ct ON c.client_id = ct.client_id
CROSS JOIN overall_avg oa;
