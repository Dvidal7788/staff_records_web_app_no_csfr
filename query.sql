.schema

-- CREATE TABLE IF NOT EXISTS users (
--     user_id INTEGER NOT NULL,
--     username TEXT NOT NULL,
--     hash,
--     PRIMARY KEY(user_id)
-- );

-- CREATE TABLE IF NOT EXISTS staff (
--     emp_id INTEGER NOT NULL,
--     name TEXT NOT NULL,
--     department TEXT,
--     start_date DATE,
--     PRIMARY KEY(emp_id)
-- );


-- DROP TABLE users;
-- DROP TABLE staff;

-- INSERT INTO users VALUES(1,'dave123','test_hash1234efef');
-- INSERT INTO staff VALUES (0,'dave', 'director', '2023-02-15');

-- SELECT * FROM users;
SELECT * FROM staff;

-- DELETE FROM users;
-- DELETE FROM staff;

-------------------------
-- BACKEND:
-- DROP TABLE departments_sort;

-- CREATE TABLE IF NOT EXISTS manager_pin (
--     hash TEXT
-- );

-- SELECT * FROM manager_pin