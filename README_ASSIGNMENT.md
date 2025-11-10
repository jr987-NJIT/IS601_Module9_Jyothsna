# Module 9 Assignment: Docker Compose with PostgreSQL and pgAdmin
## FastAPI Calculator with Database Integration

---

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Project Structure](#project-structure)
4. [Setup Instructions](#setup-instructions)
5. [Accessing pgAdmin](#accessing-pgadmin)
6. [SQL Operations Guide](#sql-operations-guide)
7. [Screenshot Documentation Guide](#screenshot-documentation-guide)
8. [Troubleshooting](#troubleshooting)
9. [Submission Checklist](#submission-checklist)

---

## Overview

This assignment demonstrates the integration of FastAPI with PostgreSQL database using Docker Compose. You will:
- Set up a multi-container environment (FastAPI, PostgreSQL, pgAdmin)
- Create database tables with relationships
- Perform CRUD operations (Create, Read, Update, Delete)
- Document all operations with screenshots

---

## Prerequisites

Before starting, ensure you have:
- Docker Desktop installed and running
- Git installed
- Basic understanding of SQL
- A text editor or IDE (VS Code recommended)

---

## Project Structure

```
IS601_Module9_Jyothsna/
├── docker-compose.yml          # Multi-service configuration
├── Dockerfile                  # FastAPI container configuration
├── main.py                     # FastAPI application
├── requirements.txt            # Python dependencies
├── sql_scripts.sql             # All SQL commands for the assignment
├── README_ASSIGNMENT.md        # This file
├── app/
│   └── operations/
│       └── __init__.py
├── templates/
│   └── index.html
└── tests/
    ├── conftest.py
    ├── e2e/
    ├── integration/
    └── unit/
```

---

## Setup Instructions

### Step 1: Verify Docker Installation

Open PowerShell and verify Docker is installed:

```powershell
docker --version
docker-compose --version
```

### Step 2: Navigate to Project Directory

```powershell
cd C:\Users\HP\Desktop\Module9\IS601_Module8_Jyothsna
```

### Step 3: Build and Start All Services

Run the following command to build and start all containers:

```powershell
docker-compose up --build
```

**What happens:**
- PostgreSQL database starts on port 5432
- pgAdmin web interface starts on port 5050
- FastAPI application starts on port 8000

**Expected output:**
```
Creating postgres_db ... done
Creating pgadmin ... done
Creating fastapi_calculator ... done
```

### Step 4: Verify Services are Running

In a new PowerShell window, run:

```powershell
docker ps
```

You should see three containers running:
1. `postgres_db`
2. `pgadmin`
3. `fastapi_calculator`

**📸 SCREENSHOT #1: Take a screenshot showing all three containers running**

---

## Accessing pgAdmin

### Step 1: Open pgAdmin in Browser

1. Open your web browser
2. Navigate to: `http://localhost:5050`

**📸 SCREENSHOT #2: Take a screenshot of the pgAdmin login page**

### Step 2: Login to pgAdmin

Use the following credentials:
- **Email:** `admin@admin.com`
- **Password:** `admin`

**📸 SCREENSHOT #3: Take a screenshot after successful login**

### Step 3: Register PostgreSQL Server

1. Right-click on "Servers" in the left panel
2. Select **Create** > **Server...**

**General Tab:**
- **Name:** `FastAPI Database`

**Connection Tab:**
- **Host name/address:** `db` (this is the Docker service name)
- **Port:** `5432`
- **Maintenance database:** `fastapi_db`
- **Username:** `postgres`
- **Password:** `postgres`
- **Save password:** Check this box

3. Click **Save**

**📸 SCREENSHOT #4: Take a screenshot of the server registration form**

**📸 SCREENSHOT #5: Take a screenshot showing the server successfully connected**

### Step 4: Open Query Tool

1. Expand the server tree: **FastAPI Database** > **Databases** > **fastapi_db**
2. Right-click on **fastapi_db**
3. Select **Query Tool**

**📸 SCREENSHOT #6: Take a screenshot of the Query Tool window**

---

## SQL Operations Guide

Now you'll execute each SQL operation from the `sql_scripts.sql` file. For each section, copy the SQL commands into the Query Tool and execute them.

### (A) Create Tables

**Operation:** Create `users` and `calculations` tables

```sql
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
```

**Steps:**
1. Copy the SQL above
2. Paste it into the Query Tool
3. Click the **Execute** button (▶️) or press F5

**Expected Result:** `Query returned successfully in X msec.`

**📸 SCREENSHOT #7: Create Tables - Show the query and success message**

**Verification:**
- Refresh the database tree
- Expand **Schemas** > **public** > **Tables**
- You should see `users` and `calculations` tables

**📸 SCREENSHOT #8: Show the tables in the database tree**

---

### (B) Insert Records

**Operation:** Add sample users and calculations

```sql
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
```

**Steps:**
1. Copy the SQL above
2. Paste it into the Query Tool
3. Execute the query

**Expected Result:** `INSERT 0 2` (for users) and `INSERT 0 3` (for calculations)

**📸 SCREENSHOT #9: Insert Records - Show the query and success message**

---

### (C) Query Data

#### Query 1: Retrieve All Users

```sql
SELECT * FROM users;
```

**Expected Result:** 2 rows showing Alice and Bob with their IDs, emails, and timestamps

**📸 SCREENSHOT #10: Query All Users - Show the query and results table**

#### Query 2: Retrieve All Calculations

```sql
SELECT * FROM calculations;
```

**Expected Result:** 3 rows showing all calculations with operations, operands, results, and user IDs

**📸 SCREENSHOT #11: Query All Calculations - Show the query and results table**

#### Query 3: Join Users and Calculations

```sql
SELECT u.username, c.operation, c.operand_a, c.operand_b, c.result
FROM calculations c
JOIN users u ON c.user_id = u.id;
```

**Expected Result:** 3 rows showing username with each calculation

**📸 SCREENSHOT #12: Join Query - Show the query and results demonstrating the relationship**

**This demonstrates the one-to-many relationship between users and calculations!**

---

### (D) Update a Record

**Operation:** Update the result of calculation ID 1

```sql
UPDATE calculations
SET result = 6
WHERE id = 1;

-- Verify the update
SELECT * FROM calculations WHERE id = 1;
```

**Expected Result:** 
- Update returns: `UPDATE 1`
- SELECT shows the calculation with result = 6 (changed from 5)

**📸 SCREENSHOT #13: Update Record - Show both the UPDATE command and verification SELECT**

---

### (E) Delete a Record

**Operation:** Delete calculation ID 2

```sql
DELETE FROM calculations
WHERE id = 2;

-- Verify the deletion
SELECT * FROM calculations;
```

**Expected Result:** 
- Delete returns: `DELETE 1`
- SELECT shows only 2 calculations remaining (IDs 1 and 3)

**📸 SCREENSHOT #14: Delete Record - Show both the DELETE command and verification SELECT**

---

### Additional Queries (Optional - for extra credit)

#### View Remaining Data with Join

```sql
SELECT u.username, c.operation, c.operand_a, c.operand_b, c.result, c.timestamp
FROM calculations c
JOIN users u ON c.user_id = u.id
ORDER BY c.timestamp DESC;
```

**📸 SCREENSHOT #15 (Optional): Final state of data after all operations**

#### Count Calculations Per User

```sql
SELECT u.username, COUNT(c.id) as calculation_count
FROM users u
LEFT JOIN calculations c ON u.id = c.user_id
GROUP BY u.username;
```

**📸 SCREENSHOT #16 (Optional): Aggregated data showing calculation counts**

---

## Screenshot Documentation Guide

### Creating Your Word Document

Create a Word document with the following structure:

**Title Page:**
- Assignment Title: Module 9 - Docker Compose with PostgreSQL
- Your Name
- Date
- Course: IS601

**For Each Screenshot Include:**
1. **Section Number and Title** (e.g., "Screenshot #7: Create Tables")
2. **The Screenshot Image**
3. **Caption/Description** (2-3 sentences explaining what the screenshot shows)
4. **Observation** (What did you learn from this step?)

**Example Format:**

```
Screenshot #7: Create Tables
[INSERT SCREENSHOT HERE]

Caption: This screenshot shows the successful execution of CREATE TABLE commands 
for the users and calculations tables. The Query Tool displays the SQL commands 
and confirms successful execution with the message "Query returned successfully."

Observation: I learned how to create tables with primary keys, constraints, and 
foreign key relationships. The SERIAL type automatically generates sequential IDs, 
and the FOREIGN KEY constraint ensures referential integrity between tables.
```

---

## Troubleshooting

### Issue: Cannot Access pgAdmin at localhost:5050

**Solution:**
1. Verify containers are running: `docker ps`
2. Check if port 5050 is in use: `netstat -ano | findstr :5050`
3. Restart Docker Desktop
4. Rebuild containers: `docker-compose down` then `docker-compose up --build`

### Issue: Cannot Connect to PostgreSQL Server in pgAdmin

**Solution:**
1. Ensure you're using `db` as the hostname (not `localhost`)
2. Verify credentials: username=`postgres`, password=`postgres`
3. Check that the postgres_db container is running

### Issue: Foreign Key Constraint Violation

**Solution:**
- Ensure you create the `users` table BEFORE the `calculations` table
- Ensure you insert users BEFORE inserting calculations
- The user_id in calculations must reference an existing user

### Issue: "Relation already exists" Error

**Solution:**
- Tables already exist. You can either:
  - Drop them first: `DROP TABLE calculations, users;`
  - Or create fresh database by removing volumes: `docker-compose down -v`

---

## Submission Checklist

### Required Files:

- ✅ **GitHub Repository Link**
  - Ensure all files are pushed to GitHub
  - Include updated `docker-compose.yml`
  - Include `sql_scripts.sql`
  - Include this `README_ASSIGNMENT.md`

- ✅ **Word Document / PDF** with:
  - Title page with your information
  - Minimum 14 screenshots (required operations)
  - Each screenshot with caption and observation
  - Properly formatted and professional appearance

### Screenshot Checklist:

1. ✅ Docker containers running (3 containers)
2. ✅ pgAdmin login page
3. ✅ pgAdmin dashboard after login
4. ✅ Server registration form
5. ✅ Server successfully connected
6. ✅ Query Tool window
7. ✅ CREATE TABLES execution and result
8. ✅ Tables visible in database tree
9. ✅ INSERT statements execution
10. ✅ SELECT all users query result
11. ✅ SELECT all calculations query result
12. ✅ JOIN query result (demonstrating relationship)
13. ✅ UPDATE statement and verification
14. ✅ DELETE statement and verification
15. ✅ (Optional) Final state with JOIN
16. ✅ (Optional) Aggregation query

### Reflection Document:

Include a separate section in your Word document addressing:

1. **What did you learn?**
   - Docker Compose multi-container orchestration
   - PostgreSQL database operations
   - Using pgAdmin for database management
   - SQL CRUD operations
   - Database relationships (one-to-many)

2. **Challenges Faced:**
   - Any difficulties during setup
   - How you resolved them
   - Resources you consulted

3. **Key Takeaways:**
   - Importance of containerization
   - Benefits of using Docker for database development
   - Understanding of foreign key relationships
   - SQL proficiency improvements

---

## Stopping the Environment

When you're done:

```powershell
# Stop all containers
docker-compose down

# Stop and remove volumes (clears database data)
docker-compose down -v
```

---

## Additional Resources

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [pgAdmin Documentation](https://www.pgadmin.org/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

## Learning Outcomes Addressed

✅ **CLO9:** Apply containerization techniques to containerize applications using Docker
- Configured multi-container environment with Docker Compose
- Used Docker volumes for data persistence
- Implemented Docker networking between services

✅ **CLO11:** Integrate Python programs with SQL databases to create and manipulate data
- Connected FastAPI application to PostgreSQL
- Performed CRUD operations on database
- Implemented database relationships with foreign keys

---

## Contact

If you encounter any issues or have questions:
1. Review the Troubleshooting section
2. Check Docker and pgAdmin logs
3. Consult course materials
4. Reach out to instructor or TA

---

**Good luck with your assignment! 🚀**
