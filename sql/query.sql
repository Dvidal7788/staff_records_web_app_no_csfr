-- STAFF ----

-- .schema

-- CSV
-- .mode csv
-- .header on
-- .output staff_test2.csv
-- SELECT * FROM staff;
-- .quit


-- COLUMN NAME:
-- SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('staff');
-- SELECT sql FROM sqlite_master
-- WHERE tbl_name = 'staff' AND type = 'table'

-- PRAGMA table_info(staff);
-- PRAGMA table_info(staff);
-- SELECT name FROM pragma_table_info('staff')
-- SELECT name FROM PRAGMA_TABLE_INFO('staff');


-- CREATE TABLE IF NOT EXISTS staff (
--     emp_id INTEGER UNIQUE NOT NULL,
--     first_name VARCHAR(30) NOT NULL,
--     last_name VARCHAR(30) NOT NULL,
--     department VARCHAR(30),
--     title VARCHAR(30),
--     start_date DATE,
--     PRIMARY KEY(emp_id)
-- );

-- CREATE TABLE IF NOT EXISTS salary (
--     emp_id INTEGER UNIQUE NOT NULL,
--     salary MONEY NOT NULL,
--     FOREIGN KEY(emp_id) REFERENCES staff(emp_id) ON DELETE CASCADE
-- );

-- CREATE TABLE IF NOT EXISTS departments (
--     department VARCHAR(30)
-- );

-- CREATE TABLE IF NOT EXISTS former_staff (
--     emp_id INTEGER UNIQUE NOT NULL,
--     first_name VARCHAR(30) NOT NULL,
--     last_name VARCHAR(30) NOT NULL,
--     department VARCHAR(30),
--     reason_for_leaving VARCHAR(30) NOT NULL,
--     start_date DATE,
--     end_date DATE,
--     notes VARCHAR(100)
-- );


-- DROP TABLE staff;
-- DROP TABLE salary;
-- DROP TABLE departments;
-- DROP TABLE former_staff;

-- ALTER TABLE departmnents RENAME TO departments;

-- INSERT INTO departments (department) VALUES('board of directors');
-- INSERT INTO departments VALUES('accounting');
-- INSERT INTO departments VALUES('administration');
-- INSERT INTO departments VALUES('client implementation');
-- INSERT INTO departments VALUES('marketing');
-- INSERT INTO departments VALUES('human resources');
-- INSERT INTO departments VALUES('it');
-- INSERT INTO departments VALUES('sales');


-- SELECT salary.emp_id, salary, first_name, last_name, department, title, start_date FROM salary JOIN staff on salary.emp_id = staff.emp_id;

-- DROP TABLE staff;
-- DROP table salary;
-- DROP TABLE departments;
-- DROP TABLE former_staff;


-- INSERT INTO staff VALUES (24,'david', 'forrester', 'sales', 'sales manager', '2022-10-10');
-- INSERT INTO salary VALUES (24, 90000);

-- INSERT INTO salary VALUES (0, 250000);
-- INSERT INTO salary VALUES (1, 250000);
-- INSERT INTO salary VALUES (2, 65000.85);
-- INSERT INTO salary VALUES (3, 80000);
-- INSERT INTO salary VALUES (4, 80000);
-- INSERT INTO salary VALUES (5, 90000);
-- INSERT INTO salary VALUES (6, 70000);
-- INSERT INTO salary VALUES (7, 60000);
-- INSERT INTO salary VALUES (8, 95000);
-- INSERT INTO salary VALUES (9, 70000);
-- INSERT INTO salary VALUES (10, 85000);
-- INSERT INTO salary VALUES (11, 65000);
-- INSERT INTO salary VALUES (12, 85000);
-- INSERT INTO salary VALUES (13, 100000);
-- INSERT INTO salary VALUES (14, 90000);
-- INSERT INTO salary VALUES (15, 90000);
-- INSERT INTO salary VALUES (16, 75000);
-- INSERT INTO salary VALUES (17, 75000);
-- INSERT INTO salary VALUES (18, 75000);
-- INSERT INTO salary VALUES (19, 75000);
-- INSERT INTO salary VALUES (20, 65000);
-- INSERT INTO salary VALUES (21, 75000);
-- INSERT INTO salary VALUES (22, 75000);
-- INSERT INTO salary VALUES (23, 65000);
-- INSERT INTO salary VALUES (25, 80000);
-- INSERT INTO salary VALUES (26, 90000);




-- SELECT * FROM staff;
-- SELECT * FROM salary;
-- SELECT * FROM former_staff;
UPDATE salary SET salary = 95000 WHERE emp_id = 26;

-- SELECT * FROM departments;


-- ALTER TABLE former_employees
-- RENAME TO former_staff;

-- DELETE FROM staff WHERE emp_id = 24;
-- DELETE FROM salary WHERE emp_id = 33 OR emp_id = 34;
-- DELETE FROM former_staff WHERE emp_id = 24;
-- DELETE FROM staff WHERE last_name = 'huang' OR last_name = 'naim';


-- DELETE FROM salary WHERE emp_id = 24;

-- DELETE FROM salary;
-- DELETE FROM former_staff;

-------------------------
-- BACKEND:
-- .schema

-- CREATE TABLE IF NOT EXISTS users (
--     user_id INTEGER NOT NULL,
--     username TEXT NOT NULL,
--     pw_hash NOT NULL,
--     security_question VARCHAR(50),
--     security_answer VARCHAR(30),
--     PRIMARY KEY(user_id)
-- );

-- CREATE TABLE IF NOT EXISTS manager_pin (
--     hash TEXT
-- );

-- ALTER TABLE users
-- ADD COLUMN security_question VARCHAR(50);

-- ALTER TABLE users
-- ADD COLUMN
-- security_answer VARCHAR(30);


-- DELETE FROM users;
-- DELETE FROM manager_pin;

-- -- DROP
-- DROP TABLE users;
-- DROP TABLE manager_pin;


-- SELECT security_question FROM users;
-- SELECT * FROM users;
-- SELECT * FROM manager_pin;


-- INSERT INTO manager