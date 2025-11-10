# Screenshot Guide for Module 9 Assignment
## Complete Checklist and Tips

---

## Taking Screenshots on Windows

### Method 1: Snipping Tool (Recommended)
1. Press `Windows Key + Shift + S`
2. Select the area to capture
3. Screenshot is copied to clipboard
4. Paste into Word document with `Ctrl + V`

### Method 2: Full Screen
1. Press `PrtScn` (Print Screen) key
2. Opens Snipping Tool automatically
3. Save or paste into document

### Method 3: Active Window
1. Press `Alt + PrtScn`
2. Captures only the active window
3. Paste into document

---

## Complete Screenshot Checklist

### Phase 1: Environment Setup

#### ✅ Screenshot #1: Docker Containers Running
**When to Take:** After running `docker-compose up --build`

**PowerShell Command:**
```powershell
docker ps
```

**What to Capture:**
- The entire PowerShell window showing `docker ps` output
- All three containers visible:
  - postgres_db (port 5432)
  - pgadmin (port 80->5050)
  - fastapi_calculator (port 8000)
- STATUS column showing "Up" for all containers

**Caption Template:**
"Docker Compose successfully started three containers: PostgreSQL database (postgres_db), pgAdmin web interface (pgadmin), and FastAPI application (fastapi_calculator). All containers are running and healthy."

---

### Phase 2: pgAdmin Access

#### ✅ Screenshot #2: pgAdmin Login Page
**When to Take:** When you first navigate to http://localhost:5050

**What to Capture:**
- Browser address bar showing `localhost:5050`
- pgAdmin login form with email and password fields
- pgAdmin logo and branding

**Caption Template:**
"The pgAdmin login page is accessible at localhost:5050. This web-based interface allows us to manage PostgreSQL databases through a graphical user interface."

---

#### ✅ Screenshot #3: pgAdmin Dashboard After Login
**When to Take:** Immediately after logging in with admin@admin.com / admin

**What to Capture:**
- Full pgAdmin interface
- Welcome screen or dashboard
- Left sidebar with "Servers" option
- Navigation menu at top

**Caption Template:**
"Successfully logged into pgAdmin. The dashboard provides access to database servers, query tools, and database management features."

---

#### ✅ Screenshot #4: Server Registration Form
**When to Take:** When creating new server connection

**What to Capture:**
- The "Create - Server" dialog box
- General tab with Name field filled: "FastAPI Database"
- Connection tab visible (switch to this tab for better screenshot)
- All connection details filled in:
  - Host: db
  - Port: 5432
  - Maintenance database: fastapi_db
  - Username: postgres
  - Password: ******* (hidden)

**Caption Template:**
"Registering the PostgreSQL server in pgAdmin. The hostname is 'db' (Docker service name), connecting to the fastapi_db database on port 5432 using the postgres user account."

---

#### ✅ Screenshot #5: Server Successfully Connected
**When to Take:** After clicking Save and server appears in left panel

**What to Capture:**
- Left sidebar showing "Servers" expanded
- "FastAPI Database" server listed and connected (green dot icon)
- Database hierarchy partially expanded showing fastapi_db

**Caption Template:**
"The PostgreSQL server is successfully connected in pgAdmin. The green indicator shows an active connection to the database server running in the Docker container."

---

#### ✅ Screenshot #6: Query Tool Window
**When to Take:** After opening Query Tool (Right-click fastapi_db → Query Tool)

**What to Capture:**
- Full Query Tool window
- SQL editor pane (top section)
- Output/Results pane (bottom section)
- Toolbar with Execute button visible
- Database breadcrumb showing "fastapi_db" in title

**Caption Template:**
"The Query Tool provides an interface for writing and executing SQL commands. The editor pane is ready to accept SQL queries, and results will display in the bottom panel."

---

### Phase 3: CREATE Operations

#### ✅ Screenshot #7: Create Tables Execution
**When to Take:** After executing CREATE TABLE commands

**What to Capture:**
- Query Tool with both CREATE TABLE statements visible in editor
- Success message in Messages tab: "Query returned successfully"
- Execution time shown

**SQL to Show:**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

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

**Caption Template:**
"Successfully created two tables: 'users' and 'calculations'. The users table has a primary key (id) and unique constraints on username and email. The calculations table includes a foreign key reference to users(id) with CASCADE delete, establishing a one-to-many relationship."

---

#### ✅ Screenshot #8: Tables in Database Tree
**When to Take:** After refreshing the database tree view

**What to Capture:**
- Left sidebar showing database hierarchy
- Expand: Servers → FastAPI Database → Databases → fastapi_db → Schemas → public → Tables
- Both tables visible:
  - calculations
  - users
- Right-click menu or properties panel (optional)

**Caption Template:**
"The database tree view confirms both tables were created successfully under the public schema. The calculations table with its foreign key constraint is now part of the database structure."

---

### Phase 4: INSERT Operations

#### ✅ Screenshot #9: Insert Records
**When to Take:** After executing INSERT statements

**What to Capture:**
- Query Tool showing both INSERT statements
- Messages tab showing:
  - "INSERT 0 2" (for users)
  - "INSERT 0 3" (for calculations)
- Execution time

**SQL to Show:**
```sql
INSERT INTO users (username, email) 
VALUES 
('alice', 'alice@example.com'), 
('bob', 'bob@example.com');

INSERT INTO calculations (operation, operand_a, operand_b, result, user_id)
VALUES
('add', 2, 3, 5, 1),
('divide', 10, 2, 5, 1),
('multiply', 4, 5, 20, 2);
```

**Caption Template:**
"Successfully inserted 2 users (Alice and Bob) and 3 calculation records. The user_id in calculations references the id from the users table, demonstrating the foreign key relationship."

---

### Phase 5: SELECT Operations

#### ✅ Screenshot #10: Query All Users
**When to Take:** After executing SELECT * FROM users

**What to Capture:**
- SQL query visible: `SELECT * FROM users;`
- Data Output tab showing results table
- All columns visible: id, username, email, created_at
- Both rows (alice and bob)
- Row count indicator at bottom

**Caption Template:**
"Retrieved all records from the users table. The query returns 2 rows showing Alice (id=1) and Bob (id=2) with their email addresses and account creation timestamps."

---

#### ✅ Screenshot #11: Query All Calculations
**When to Take:** After executing SELECT * FROM calculations

**What to Capture:**
- SQL query visible: `SELECT * FROM calculations;`
- Data Output tab showing results table
- All columns: id, operation, operand_a, operand_b, result, timestamp, user_id
- All 3 rows visible
- Variety of operations shown (add, divide, multiply)

**Caption Template:**
"Retrieved all calculation records. The results show 3 calculations: two belonging to user_id=1 (Alice) and one to user_id=2 (Bob), demonstrating the one-to-many relationship."

---

#### ✅ Screenshot #12: JOIN Query
**When to Take:** After executing the JOIN query

**What to Capture:**
- Full JOIN query visible in editor
- Results showing combined data from both tables
- Columns: username, operation, operand_a, operand_b, result
- All 3 rows showing usernames with their calculations

**SQL to Show:**
```sql
SELECT u.username, c.operation, c.operand_a, c.operand_b, c.result
FROM calculations c
JOIN users u ON c.user_id = u.id;
```

**Caption Template:**
"The JOIN query demonstrates the one-to-many relationship between users and calculations. Alice's username appears twice (for her two calculations), while Bob's appears once. This query combines data from both tables using the foreign key relationship."

---

### Phase 6: UPDATE Operation

#### ✅ Screenshot #13: Update Record
**When to Take:** After executing UPDATE and verification SELECT

**What to Capture:**
- UPDATE statement visible
- Success message: "UPDATE 1"
- Verification SELECT query results
- Row with id=1 showing result changed from 5 to 6

**SQL to Show:**
```sql
UPDATE calculations
SET result = 6
WHERE id = 1;

SELECT * FROM calculations WHERE id = 1;
```

**Caption Template:**
"Updated the result of calculation id=1 from 5 to 6. The UPDATE statement affected 1 row, and the verification query confirms the change was successful. This demonstrates modifying existing data in the database."

---

### Phase 7: DELETE Operation

#### ✅ Screenshot #14: Delete Record
**When to Take:** After executing DELETE and verification SELECT

**What to Capture:**
- DELETE statement visible
- Success message: "DELETE 1"
- Verification SELECT showing remaining records
- Only 2 rows remain (ids 1 and 3, with id 2 deleted)

**SQL to Show:**
```sql
DELETE FROM calculations
WHERE id = 2;

SELECT * FROM calculations;
```

**Caption Template:**
"Deleted calculation record with id=2 (the divide operation). The DELETE statement removed 1 row, and the verification query shows only 2 calculations remain in the table."

---

### Phase 8: Optional Advanced Queries

#### ✅ Screenshot #15: Final State with JOIN (Optional)
**When to Take:** After executing final JOIN query

**What to Capture:**
- JOIN query with ORDER BY
- Results showing remaining data after update and delete
- Timestamps visible
- Only 2 calculations remain

**SQL to Show:**
```sql
SELECT u.username, c.operation, c.operand_a, c.operand_b, c.result, c.timestamp
FROM calculations c
JOIN users u ON c.user_id = u.id
ORDER BY c.timestamp DESC;
```

**Caption Template:**
"Final state of the database after all CRUD operations. The JOIN query shows Alice's updated calculation (result=6) and Bob's multiplication calculation. The divide operation (id=2) has been successfully deleted."

---

#### ✅ Screenshot #16: Aggregation Query (Optional)
**When to Take:** After executing COUNT query

**What to Capture:**
- Aggregation query with GROUP BY
- Results showing calculation counts per user
- Alice: 1 calculation
- Bob: 1 calculation

**SQL to Show:**
```sql
SELECT u.username, COUNT(c.id) as calculation_count
FROM users u
LEFT JOIN calculations c ON u.id = c.user_id
GROUP BY u.username;
```

**Caption Template:**
"Aggregation query demonstrating SQL's analytical capabilities. Using COUNT and GROUP BY, we can see how many calculations each user has performed. Both users now have 1 calculation each after our CRUD operations."

---

## Screenshot Quality Tips

### ✅ DO:
- Use high resolution (1920x1080 or higher)
- Capture clear, readable text
- Include relevant context (toolbars, labels)
- Show complete SQL statements
- Include success messages
- Crop out unnecessary desktop clutter
- Use full window captures for context

### ❌ DON'T:
- Take blurry screenshots
- Cut off important information
- Include personal/sensitive information
- Use low resolution
- Have cluttered backgrounds
- Forget to show the SQL query with results

---

## Organizing Screenshots in Word Document

### Document Structure:

```
MODULE 9 ASSIGNMENT: DATABASE OPERATIONS WITH DOCKER & POSTGRESQL
Student Name
Date
Course

TABLE OF CONTENTS

1. ENVIRONMENT SETUP
   Screenshot #1: Docker Containers Running
   [Image]
   [Caption]
   [Observation]

2. PGADMIN ACCESS
   Screenshot #2: Login Page
   Screenshot #3: Dashboard
   Screenshot #4: Server Registration
   Screenshot #5: Connected Server
   Screenshot #6: Query Tool

3. CREATE OPERATIONS
   Screenshot #7: Create Tables
   Screenshot #8: Tables in Database

4. INSERT OPERATIONS
   Screenshot #9: Insert Records

5. SELECT OPERATIONS (QUERIES)
   Screenshot #10: All Users
   Screenshot #11: All Calculations
   Screenshot #12: JOIN Query

6. UPDATE OPERATIONS
   Screenshot #13: Update and Verify

7. DELETE OPERATIONS
   Screenshot #14: Delete and Verify

8. OPTIONAL QUERIES
   Screenshot #15: Final State
   Screenshot #16: Aggregation

REFLECTION
[Your reflection content]
```

---

## Quick Reference: All SQL Commands

Copy this into Query Tool and execute section by section:

```sql
-- ========== CREATE TABLES ==========
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

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

-- ========== INSERT RECORDS ==========
INSERT INTO users (username, email) 
VALUES 
('alice', 'alice@example.com'), 
('bob', 'bob@example.com');

INSERT INTO calculations (operation, operand_a, operand_b, result, user_id)
VALUES
('add', 2, 3, 5, 1),
('divide', 10, 2, 5, 1),
('multiply', 4, 5, 20, 2);

-- ========== QUERY DATA ==========
SELECT * FROM users;

SELECT * FROM calculations;

SELECT u.username, c.operation, c.operand_a, c.operand_b, c.result
FROM calculations c
JOIN users u ON c.user_id = u.id;

-- ========== UPDATE RECORD ==========
UPDATE calculations
SET result = 6
WHERE id = 1;

SELECT * FROM calculations WHERE id = 1;

-- ========== DELETE RECORD ==========
DELETE FROM calculations
WHERE id = 2;

SELECT * FROM calculations;

-- ========== OPTIONAL QUERIES ==========
SELECT u.username, c.operation, c.operand_a, c.operand_b, c.result, c.timestamp
FROM calculations c
JOIN users u ON c.user_id = u.id
ORDER BY c.timestamp DESC;

SELECT u.username, COUNT(c.id) as calculation_count
FROM users u
LEFT JOIN calculations c ON u.id = c.user_id
GROUP BY u.username;
```

---

## Common Issues and How to Screenshot Them

### If Something Goes Wrong:

1. **Error Messages**: Capture the full error text
2. **Troubleshooting Steps**: Screenshot your solution process
3. **Before/After**: Show the problem and the fix

These can be valuable additions to your reflection!

---

## Final Checklist Before Submission

- [ ] All 14 required screenshots taken
- [ ] Each screenshot is clear and readable
- [ ] SQL queries visible in screenshots
- [ ] Success messages/results visible
- [ ] Screenshots properly labeled with numbers
- [ ] Captions written for each screenshot
- [ ] Observations/learning notes added
- [ ] Document professionally formatted
- [ ] Reflection section completed
- [ ] Converted to PDF (if required)
- [ ] File named appropriately (e.g., "Module9_YourName.pdf")

---

**You're ready to complete the assignment! Good luck! 🎯**
