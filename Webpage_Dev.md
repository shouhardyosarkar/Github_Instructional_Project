Webpage Development with GitHub
==============================================================

## 1️⃣ What Is Webpage Development?

Webpage development involves creating and maintaining websites using languages such as HTML, CSS, and JavaScript. In the context of GitHub, it refers to building, storing, and hosting your website projects directly within GitHub repositories.

💡 Think of GitHub as both your workspace and your deployment platform for web projects.

**Key concepts:**
- Develop and organize website files (HTML, CSS, JS)
- Use Git for version tracking and collaboration
- Deploy static sites using GitHub Pages

---

## 2️⃣ Why Use GitHub for Webpage Development?

- Simplifies **project hosting** with GitHub Pages  
- Supports **version control**, so every change is tracked  
- Enables **team collaboration** through pull requests and branching  
- Integrates easily with tools like **Jekyll** and static site generators  
- Provides **free, reliable web hosting** for personal or project sites  

---

## 3️⃣ What Is GitHub Pages?

**GitHub Pages** is a feature that lets you host static websites directly from your repository.  
Once enabled, GitHub automatically publishes your code as a live webpage.

**Example:**  
If your repository is named `portfolio`, your site might appear at  
`https://username.github.io/portfolio`

**Supports:**
- Plain HTML/CSS/JS projects  
- Markdown and Jekyll sites (great for blogs or documentation)  
- Custom domain names  

---

## 4️⃣ Step-by-Step Webpage Setup
### Add Website Files

1. Create a simple homepage:

   **index.html**
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1" />
       <title>My GitHub Pages Site</title>
       <link rel="stylesheet" href="styles.css" />
     </head>
     <body>
       <main>
         <h1>Hello, GitHub Pages 👋</h1>
         <p>This site is deployed from a GitHub repository.</p>
       </main>
       <script src="main.js"></script>
     </body>
   </html>
   ```

2. Add and commit the files:
	
	- Save html script as **index.html**.
	- Click 'Add File' and Commit index.html to the repo.

---
### Enable GitHub Pages

1. On your repo, go to **Settings → Pages**  
2. **Source**: choose the branch and folder to publish
   - Publish the **`main`** branch, root (/) or /docs
3. Click **Save**  
4. Wait for “Your site is live at …” banner (first publish can take a minute)

> URL patterns:  
> - User site: `https://USERNAME.github.io/`  
> - Project site: `https://USERNAME.github.io/REPO-NAME/`
---
### Verify and Add Basics
- Visit your site URL to confirm it loads
- Add helpful extras (optional but recommended):
  - **favicon.ico** or `site.webmanifest`
  - **/404.html** (custom not-found page)
  - **/CNAME** (only if using a custom domain)
  - **robots.txt** (if you want to control indexing)

---
### Troubleshooting
- **404 or old content:** wait 1–2 minutes; hard-refresh (Ctrl/Cmd+Shift+R).  
- **Wrong paths on Project Sites:** ensure correct base path (`/REPO-NAME/`).    
- **Private repo:** GitHub Pages requires public visibility for anonymous visitors (unless using Enterprise with internal pages).

---
### Daily Workflow (Maintain Your Site)
- Edit files locally → `git add -A` → `git commit -m "Change"` → `git push`  
- Use **branches + pull requests** for team review  
- Keep content in `/docs` or `main` 

---
## 5️⃣ Why It Matters

Using GitHub for webpage development helps you:
- Build a **portfolio** to showcase skills  
- Host **documentation** for projects  
- Learn professional **version control workflows**  
- Contribute to **open-source** web projects  

