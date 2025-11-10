-- =============================================
-- SQL Scripts for Module 9 Assignment
-- FastAPI + PostgreSQL Database Operations
-- =============================================

-- =============================================
-- (A) CREATE TABLES
-- =============================================

-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create calculations table with foreign key to users
CREATE TABLE calculations (
    id SERIAL PRIMARY KEY,
    operation VARCHAR(20) NOT NULL,
    operand_a FLOAT NOT NULL,
    operand_b FLOAT NOT NULL,
    result FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- =============================================
-- (B) INSERT RECORDS
-- =============================================

-- Insert users
INSERT INTO users (username, email) 
VALUES 
('alice', 'alice@example.com'), 
('bob', 'bob@example.com');

-- Insert calculations
INSERT INTO calculations (operation, operand_a, operand_b, result, user_id)
VALUES
('add', 2, 3, 5, 1),
('divide', 10, 2, 5, 1),
('multiply', 4, 5, 20, 2);

-- =============================================
-- (C) QUERY DATA
-- =============================================

-- Retrieve all users
SELECT * FROM users;

-- Retrieve all calculations
SELECT * FROM calculations;

-- Join users and calculations
SELECT u.username, c.operation, c.operand_a, c.operand_b, c.result
FROM calculations c
JOIN users u ON c.user_id = u.id;

-- =============================================
-- (D) UPDATE A RECORD
-- =============================================

-- Update the result of calculation id 1
UPDATE calculations
SET result = 6
WHERE id = 1;

-- Verify the update
SELECT * FROM calculations WHERE id = 1;

-- =============================================
-- (E) DELETE A RECORD
-- =============================================

-- Delete calculation with id 2
DELETE FROM calculations
WHERE id = 2;

-- Verify the deletion
SELECT * FROM calculations;

-- =============================================
-- ADDITIONAL QUERIES (Optional)
-- =============================================

-- View all calculations with user information after update and delete
SELECT u.username, c.operation, c.operand_a, c.operand_b, c.result, c.timestamp
FROM calculations c
JOIN users u ON c.user_id = u.id
ORDER BY c.timestamp DESC;

-- Count calculations per user
SELECT u.username, COUNT(c.id) as calculation_count
FROM users u
LEFT JOIN calculations c ON u.id = c.user_id
GROUP BY u.username;
