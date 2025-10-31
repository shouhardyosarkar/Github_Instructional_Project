# 🕒 Shift Logger — Team Handoff Record System

## 📘 Overview
This Python script (`shift_log.py`) is designed for small teams to **simulate real-world handoff and monitoring workflows**.  
Each member logs their session activities and passes control to the next person. Logs are saved as `.csv` files under the `logs/` directory, allowing traceable, timestamped collaboration.

The project demonstrates **practical teamwork and version control** — multiple users contribute sequentially, push their changes to GitHub, and continue each other’s progress.

---

## ⚙️ Features
- Lists existing log files in the `logs/` folder.  
- Prompts whether to continue writing to an existing log or create a new one.  
- Automatically records metadata such as:
  - UTC timestamp
  - Username / machine name
  - System information (OS, hostname)
- Appends shift data to the chosen CSV file.  
- Supports reviewing or clearing existing logs.

---

## 🧩 Dependencies
This project only relies on Python's **standard library**.

No external installation is required, but the environment should have Python **3.8+**.


---

## 🧭 How to Use
1. Run the script:
   ```bash
   python shift_log.py
   ```

2. Choose from the interactive menu:
   - List all log files
   - Create a new log
   - Append to an existing log
   - View a CSV file’s contents
   - Delete or reset logs

3. Each entry will include:
   - Timestamp
   - User
   - Summary or handoff notes

---

## 🗂 Folder Structure
```
ShiftLog/
├── shift_log.py           # Main script
├── logs/                  # Folder where CSV logs are stored
└── README.md             # This documentation file
```

---

## 💡 Tips for Team Use
- Each team member should **pull** before running and **push** after updating:
  ```bash
  git pull origin main
  python shift_log.py
  git add logs/*.csv
  git commit -m "Add new shift log entry"
  git push origin main
  ```
- If conflicts occur, Git will guide you to merge — treat this as a real collaboration exercise.

---

## 📊 Example Log (CSV)
| Timestamp (UTC) | User | Notes |
|-----------------|------|-------|
| 2025-10-27 12:00:00 | Shuo | Monitored process stability |
| 2025-10-27 15:00:00 | Teammate | Continued data collection |

---

## 🧱 Educational Purpose
This toy project is meant to demonstrate **data collaboration, reproducibility, and teamwork** using Python and GitHub.  
It mimics lab-shift handoffs or data-monitoring workflows that require logging, accountability, and shared version control.
