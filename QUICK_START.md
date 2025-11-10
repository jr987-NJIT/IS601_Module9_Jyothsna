# 🚀 QUICK START GUIDE - Module 9 Assignment

## ⏱️ Time Estimate: 2-3 hours

---

## 📋 Pre-Flight Checklist

Before starting, ensure you have:
- [ ] Docker Desktop installed and running
- [ ] Git installed
- [ ] Microsoft Word or Google Docs for documentation
- [ ] Web browser (Chrome, Firefox, or Edge)
- [ ] 2-3 hours of uninterrupted time

---

## 🎯 5-Step Quick Start

### Step 1: Start the Environment (5 minutes)

Open PowerShell and navigate to your project:

```powershell
cd C:\Users\HP\Desktop\Module9\IS601_Module8_Jyothsna
docker-compose up --build
```

Wait for all services to start. You should see:
```
Creating postgres_db ... done
Creating pgadmin ... done
Creating fastapi_calculator ... done
```

✅ **Screenshot #1**: Run `docker ps` in a new PowerShell window

---

### Step 2: Access pgAdmin (10 minutes)

1. Open browser: http://localhost:5050
2. Login with:
   - Email: `admin@admin.com`
   - Password: `admin`

3. Create new server connection:
   - **Name**: `FastAPI Database`
   - **Host**: `db`
   - **Port**: `5432`
   - **Database**: `fastapi_db`
   - **Username**: `postgres`
   - **Password**: `postgres`

4. Open Query Tool (Right-click `fastapi_db` → Query Tool)

✅ **Screenshots #2-6**: Capture each step

---

### Step 3: Run SQL Commands (30 minutes)

Open `sql_scripts.sql` and copy each section into pgAdmin Query Tool:

**For each section:**
1. Copy SQL from the file
2. Paste into Query Tool
3. Click Execute (▶️)
4. Take screenshot of query + result

**Sections:**
- (A) Create Tables → ✅ Screenshots #7-8
- (B) Insert Records → ✅ Screenshot #9
- (C) Query Data → ✅ Screenshots #10-12
- (D) Update Record → ✅ Screenshot #13
- (E) Delete Record → ✅ Screenshot #14

---

### Step 4: Document Everything (60 minutes)

Create Word document with:

**Structure:**
```
Title Page
├── Your Name
├── Course: IS601
└── Date

Section 1: Environment Setup
├── Screenshot #1 + Caption + Observation

Section 2: pgAdmin Access
├── Screenshots #2-6 + Captions + Observations

Section 3: CREATE Operations
├── Screenshots #7-8 + Captions + Observations

Section 4: INSERT Operations
├── Screenshot #9 + Caption + Observation

Section 5: SELECT Operations
├── Screenshots #10-12 + Captions + Observations

Section 6: UPDATE Operation
├── Screenshot #13 + Caption + Observation

Section 7: DELETE Operation
├── Screenshot #14 + Caption + Observation

Reflection
├── What I Learned
├── Challenges Faced
├── Key Takeaways
└── Real-World Applications
```

---

### Step 5: Submit (15 minutes)

1. **GitHub**:
   ```powershell
   git add .
   git commit -m "Complete Module 9 Assignment"
   git push origin main
   ```

2. **Document**:
   - Save as PDF: `Module9_YourName.pdf`
   - Upload to Canvas/submission platform

3. **Final Check**:
   - [ ] All 14 screenshots included
   - [ ] Each screenshot has caption
   - [ ] Reflection completed (2-3 pages)
   - [ ] GitHub repo link included
   - [ ] Document professionally formatted

---

## 📁 Files Reference

| File | Purpose |
|------|---------|
| `docker-compose.yml` | Multi-container configuration |
| `sql_scripts.sql` | All SQL commands to run |
| `README_ASSIGNMENT.md` | Detailed instructions |
| `SCREENSHOT_GUIDE.md` | Screenshot specifications |
| `REFLECTION_TEMPLATE.md` | Reflection writing guide |
| `QUICK_START.md` | This file! |

---

## 🆘 Emergency Troubleshooting

### Problem: Can't access pgAdmin
**Solution:**
```powershell
docker-compose down
docker-compose up --build
```
Wait 30 seconds, try again.

### Problem: Can't connect to database in pgAdmin
**Fix:**
- Use hostname: `db` (NOT `localhost`)
- Username: `postgres`
- Password: `postgres`
- Database: `fastapi_db`

### Problem: "Table already exists" error
**Fix:**
```sql
DROP TABLE IF EXISTS calculations CASCADE;
DROP TABLE IF EXISTS users CASCADE;
```
Then run CREATE TABLE commands again.

### Problem: Port already in use
**Fix:**
```powershell
# Stop all containers
docker-compose down

# Check what's using the port
netstat -ano | findstr :5050
netstat -ano | findstr :5432

# Kill the process or restart Docker Desktop
```

---

## 💡 Pro Tips

1. **Take screenshots as you go** - Don't wait until the end
2. **Save SQL queries** - Keep a copy of everything you run
3. **Read error messages** - They usually tell you exactly what's wrong
4. **Use the template files** - They have all the content structure you need
5. **Start early** - Don't underestimate documentation time

---

## 📊 Grading Breakdown

| Component | Points | What to Include |
|-----------|--------|-----------------|
| GitHub Repo | 15 | All files, commits, clear README |
| Screenshots | 25 | 14 clear screenshots with captions |
| Documentation | 10 | Professional formatting |
| Reflection | 15 | 2-3 pages, thoughtful insights |
| Functionality | 35 | All SQL operations successful |
| **TOTAL** | **100** | |

---

## ✨ Going Above and Beyond

Want extra credit? Include:
- Screenshots #15-16 (advanced queries)
- Additional SQL queries you created
- Discussion of database normalization
- Comparison with other database systems
- Docker architecture diagram
- Security considerations discussion

---

## 📞 Resources

- **Full Instructions**: `README_ASSIGNMENT.md`
- **Screenshot Details**: `SCREENSHOT_GUIDE.md`
- **Reflection Help**: `REFLECTION_TEMPLATE.md`
- **SQL Commands**: `sql_scripts.sql`

---

## ⏰ Suggested Timeline

| Time | Activity |
|------|----------|
| 0:00 - 0:05 | Start Docker containers |
| 0:05 - 0:15 | Set up pgAdmin connection |
| 0:15 - 0:45 | Execute all SQL commands |
| 0:45 - 1:45 | Create Word document with screenshots |
| 1:45 - 2:30 | Write reflection |
| 2:30 - 2:45 | Final review and submission |
| 2:45 - 3:00 | Git push and submit |

---

## ✅ Success Criteria

You'll know you're successful when:
- ✅ All 3 Docker containers are running
- ✅ You can log into pgAdmin
- ✅ All SQL commands execute without errors
- ✅ You have 14+ clear screenshots
- ✅ Your document is professionally formatted
- ✅ Your reflection shows understanding
- ✅ Everything is pushed to GitHub

---

## 🎓 Learning Objectives Achieved

By completing this assignment, you will have demonstrated:

**CLO9: Containerization with Docker**
- ✅ Created multi-container environment
- ✅ Configured Docker Compose
- ✅ Managed container networking
- ✅ Used Docker volumes for persistence

**CLO11: Database Integration**
- ✅ Created database tables
- ✅ Performed CRUD operations
- ✅ Implemented foreign key relationships
- ✅ Executed JOIN queries

---

## 🚀 Ready to Start?

1. Open this folder in VS Code (or your preferred editor)
2. Open PowerShell
3. Run: `docker-compose up --build`
4. Open browser: http://localhost:5050
5. Follow the steps above!

**Good luck! You've got this! 💪**

---

## 📝 Quick Command Reference

```powershell
# Start everything
docker-compose up --build

# Stop everything
docker-compose down

# Stop and remove volumes (fresh start)
docker-compose down -v

# View running containers
docker ps

# View logs
docker-compose logs web
docker-compose logs db
docker-compose logs pgadmin

# Git commands
git status
git add .
git commit -m "Complete Module 9"
git push origin main
```

---

**Last Updated**: November 10, 2025
**Estimated Completion Time**: 2-3 hours
**Difficulty Level**: Intermediate 🎯
