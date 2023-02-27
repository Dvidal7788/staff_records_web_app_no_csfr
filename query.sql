.schema

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
--     FOREIGN KEY(emp_id) REFERENCES staff(emp_id)
-- );

-- CREATE TABLE IF NOT EXISTS departments (
--     department VARCHAR(30)
-- );


-- DROP TABLE staff;
-- DROP TABLE salary;
-- DROP TABLE departments;

-- ALTER TABLE departmnents RENAME TO departments;

-- INSERT INTO departments (department) VALUES('board of directors');
-- INSERT INTO departments VALUES('accounting');
-- INSERT INTO departments VALUES('administration');
-- INSERT INTO departments VALUES('client implementation');
-- INSERT INTO departments VALUES('marketing');
-- INSERT INTO departments VALUES('human resources');
-- INSERT INTO departments VALUES('it');
-- INSERT INTO departments VALUES('sales');


-- DROP TABLE users;
-- DROP TABLE staff;

-- INSERT INTO users VALUES(1,'dave123','test_hash1234efef');
-- INSERT INTO staff VALUES (0,'dave', 'director', '2023-02-15');


SELECT * FROM staff;
SELECT * FROM salary;

-- SELECT * FROM departments;

-- DELETE FROM users;
-- DELETE FROM staff;

-------------------------
-- BACKEND:
-- .schema

-- CREATE TABLE IF NOT EXISTS users (
--     user_id INTEGER NOT NULL,
--     username TEXT NOT NULL,
--     hash,
--     PRIMARY KEY(user_id)
-- );

-- CREATE TABLE IF NOT EXISTS manager_pin (
--     hash TEXT
-- );

-- DROP TABLE users;
-- DROP TABLE manager_pin;

-- SELECT * FROM users;
-- SELECT * FROM manager_pin;