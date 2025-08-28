/************************************************************
 * Sample Data for Basic SQL Queries
 * Python-SQL-Mini-Projects / SQL_Projects / basic_queries
 ************************************************************/

/*******************************
 * 1. Employees & Departments
 *******************************/
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO Departments (department_id, department_name) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Sales');

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2),
    department_id INT,
    manager_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES Employees(emp_id)
);

INSERT INTO Employees (emp_id, name, salary, department_id, manager_id) VALUES
(1, 'Alice', 6000, 1, NULL),
(2, 'Bob', 5500, 1, 1),
(3, 'Charlie', 7000, 2, NULL),
(4, 'David', 6800, 2, 3),
(5, 'Eve', 7200, 2, 3),
(6, 'Frank', 5000, 3, NULL),
(7, 'Grace', 4800, 3, 6);


/*******************************
 * 2. Orders
 *******************************/
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

INSERT INTO Orders (order_id, customer_id, order_date) VALUES
(1, 101, '2025-08-01'),
(2, 101, '2025-08-05'),
(3, 101, '2025-08-10'),
(4, 101, '2025-08-12'),
(5, 102, '2025-08-02'),
(6, 102, '2025-08-03'),
(7, 103, '2025-08-07');


/*******************************
 * 3. Purchases
 *******************************/
CREATE TABLE Purchases (
    purchase_id INT PRIMARY KEY,
    user_id INT,
    purchase_date DATE,
    amount DECIMAL(10,2)
);

INSERT INTO Purchases (purchase_id, user_id, purchase_date, amount) VALUES
(1, 101, '2025-08-01', 150),
(2, 101, '2025-08-03', 200),
(3, 102, '2025-08-02', 100),
(4, 103, '2025-08-05', 300),
(5, 101, '2025-08-10', 250);


/*******************************
 * 4. Visits
 *******************************/
CREATE TABLE Visits (
    user_id INT,
    visit_date DATE
);

INSERT INTO Visits (user_id, visit_date) VALUES
(101, '2025-07-28'),
(101, '2025-07-30'),
(102, '2025-07-29'),
(103, '2025-07-30');


/*******************************
 * 5. Categories (Hierarchical)
 *******************************/
CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50),
    parent_id INT
);

INSERT INTO Categories (category_id, category_name, parent_id) VALUES
(1, 'Electronics', NULL),
(2, 'Computers', 1),
(3, 'Laptops', 2),
(4, 'Smartphones', 1),
(5, 'Furniture', NULL),
(6, 'Chairs', 5);


/*******************************
 * 6. Sales
 *******************************/
CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE,
    amount DECIMAL(10,2)
);

INSERT INTO Sales (sale_id, sale_date, amount) VALUES
(1, '2025-08-01', 100),
(2, '2025-08-02', 150),
(3, '2025-08-03', 200),
(4, '2025-08-04', 120),
(5, '2025-08-05', 130),
(6, '2025-08-06', 170),
(7, '2025-08-07', 160);


/*******************************
 * 7. Users
 *******************************/
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50)
);

INSERT INTO Users (user_id, user_name) VALUES
(1, 'alice'),
(2, 'bob'),
(3, 'charlie'),
(4, 'alice'),
(5, 'bob');


/*******************************
 * 8. Weather (for consecutive cold days query)
 *******************************/
CREATE TABLE Weather (
    city VARCHAR(50),
    day DATE,
    temperature DECIMAL(5,2)
);

INSERT INTO Weather (city, day, temperature) VALUES
('London', '2025-08-01', -1),
('London', '2025-08-02', -2),
('London', '2025-08-03', -3),
('London', '2025-08-04', 2),
('Paris', '2025-08-01', 5),
('Paris', '2025-08-02', -1),
('Paris', '2025-08-03', -2);
