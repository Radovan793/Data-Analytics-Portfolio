-- Get clients that have an invoice

SELECT *
FROM clients
WHERE client_id IN (
    SELECT DISTINCT client_id
    FROM invoices
);

-- Get clients that have an invoice using EXISTS

SELECT s.*
FROM clients s
WHERE EXISTS (
    SELECT 1
    FROM invoices i
    WHERE i.client_id = s.client_id
);

-- Return every client, if there is at least one invoice over 1000

SELECT *
FROM clients
WHERE EXISTS (
    SELECT 1
    FROM invoices
    WHERE invoice_total > 1000
);

-- Find products that have never been ordered (NOT IN)

SELECT *
FROM products
WHERE product_id NOT IN (
    SELECT product_id
    FROM order_items
);

-- Safe alternative using NOT EXISTS

SELECT *
FROM products p
WHERE NOT EXISTS (
    SELECT 1
    FROM order_items oi
    WHERE oi.product_id = p.product_id
);
