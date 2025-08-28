-- Users table
CREATE TABLE users (
    user_id INT,
    user_name VARCHAR(50)
);

INSERT INTO users (user_id, user_name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Alice'),
(4, 'David');

-- Employee table
CREATE TABLE employee (
    emp_id INT,
    name VARCHAR(50),
    salary INT,
    dept_name VARCHAR(50)
);

INSERT INTO employee (emp_id, name, salary, dept_name) VALUES
(1, 'John', 70000, 'HR'),
(2, 'Jane', 85000, 'HR'),
(3, 'Tom', 60000, 'Finance'),
(4, 'Mike', 95000, 'Finance'),
(5, 'Sara', 90000, 'Finance');

-- Departments table
CREATE TABLE Departments (
    department_id INT,
    department_name VARCHAR(50)
);

INSERT INTO Departments (department_id, department_name) VALUES
(1, 'HR'),
(2, 'Finance');

-- Weather table
CREATE TABLE weather (
    city VARCHAR(50),
    day DATE,
    temperature INT
);

INSERT INTO weather (city, day, temperature) VALUES
('London', '2025-01-01', -2),
('London', '2025-01-02', -3),
('London', '2025-01-03', -1),
('London', '2025-01-04',  1),
('Paris',  '2025-01-01',  2),
('Paris',  '2025-01-02', -1),
('Paris',  '2025-01-03', -2),
('Paris',  '2025-01-04', -3);
