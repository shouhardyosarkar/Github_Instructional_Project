# 🧭 Guide: Connecting Local Folder to GitHub Repository

This document explains how to connect your **local folder** to a GitHub repository and verify that you can **push** and **pull** successfully.  
Follow these steps carefully before contributing to the project.

---

## 1️⃣ Create a New Local Folder

1. Open **File Explorer** and choose a location for your project.  
   Example:
   ```bash
   D:/Iowa_assignment/
   ```

2. Inside that directory, create a new folder for the repository:
   ```bash
   mkdir Github_Instructional_Project
   cd Github_Instructional_Project
   ```

   Alternatively, you can skip manual folder creation and clone directly (see next step).

---

## 2️⃣ Clone the Remote Repository

Run the following command in **Git Bash**, **Terminal**, or **VS Code terminal**:

```bash
git clone https://github.com/shouhardyosarkar/Github_Instructional_Project.git
```

This creates a local copy of the project on your computer.

To move into the project directory:
```bash
cd Github_Instructional_Project
```

---

## 3️⃣ Check Remote Connection

Verify that the local repository is correctly linked to GitHub:

```bash
git remote -v
```

Expected output:
```
origin  https://github.com/shouhardyosarkar/Github_Instructional_Project.git (fetch)
origin  https://github.com/shouhardyosarkar/Github_Instructional_Project.git (push)
```

If you see this, your local repository is properly connected to the remote repository.

---

## 4️⃣ Test Pull (Download Updates)

Make sure you can pull the latest changes:

```bash
git pull origin main
```

If you see:
```
Already up to date.
```
✅ It means your local copy is synchronized with GitHub.

---

## 5️⃣ Configure Authentication (if needed)

If you see an error like:
```
remote: Permission denied
fatal: Authentication failed
```

You need to log in with a **GitHub Personal Access Token (PAT)**:

1. Go to: [https://github.com/settings/tokens](https://github.com/settings/tokens)  
2. Click **“Generate new token (classic)”**  
3. Check the box for `repo` (and `workflow`, if needed)  
4. Copy the token (you’ll see it only once!)  
5. Back in your terminal, run:
   ```bash
   git config --global credential.helper store
   git pull
   ```
   Then enter your GitHub username and paste the token as the password.

---

## 6️⃣ Test Push (Upload Changes)

To verify you have write access:

```bash
echo "connection test - please ignore" > permission_check.txt
git add permission_check.txt
git commit -m "test: verify push permission"
git push origin main
```

- If successful → ✅ You have push permission.
- If rejected → ❌ Contact the repository owner to check your collaborator access.

---

## 7️⃣ Clean Up the Test File

Once confirmed, delete the test file:

```bash
git rm permission_check.txt
git commit -m "clean: remove permission_check test file"
git push origin main
```

---

## ✅ Summary

| Action | Command | Expected Result |
|---------|----------|-----------------|
| Clone repository | `git clone` | Creates local copy |
| Check remote | `git remote -v` | Shows origin URL |
| Pull | `git pull origin main` | Updates local files |
| Push | `git push origin main` | Uploads changes |
| Authentication | GitHub Token | Avoids login errors |

---

## 💡 Tips

- Always run `git pull origin main` before editing files.  
- Use `git status` to check which files have changed.  
- Use `git log --oneline` to view recent commits.
