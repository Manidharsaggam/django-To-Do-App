# 📝 Django To-Do Application

A simple and clean **To-Do List web application** built using **Django**.  
This project demonstrates full **CRUD functionality**, task completion tracking, filters, and a progress indicator — designed as a **fresher-friendly project** with real-world structure.

---

## 🚀 Features

- ➕ Add new tasks  
- ✏️ Edit tasks on the same page  
- ☑️ Mark tasks as completed / pending  
- ❌ Delete tasks  
- 🔍 Filter tasks (All / Completed / Pending)  
- 📊 Progress bar with completed task count  
- 🎨 Clean and modern UI  
- 🔒 CSRF protection  

---

## 🛠 Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite  
- **Version Control:** Git, GitHub  

---

## 📂 Project Structure

```text
ToDoList/
│
├── To_Do_App/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── todo/
│           └── task_list.html
│
├── manage.py
├── db.sqlite3
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Manidharsaggam/django-todo-app.git
cd django-todo-app

2️⃣ Create and activate virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Django
pip install django

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start the server
python manage.py runserver

6️⃣ Open in browser
http://127.0.0.1:8000/

📸 Screenshots

Home Page
![Home Page](screenshots/home.png)


Edit Page
![Home Page](screenshots/edit.png)

Completed Page
![Home Page](screenshots/completed.png)