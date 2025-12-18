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

### Clone the repository
```bash
git clone https://github.com/Manidharsaggam/django-todo-app.git
cd django-todo-app


Create and activate virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows

Install Django
pip install django

Run migrations
python manage.py makemigrations
python manage.py migrate

Start the server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

📸 Screenshots

Home Page
screenshots/home.png

Edit Task
screenshots/edit.png

Completed Task
screenshots/completed.png

🧠 What I Learned

Django CRUD operations

Handling multiple POST actions in a single view

Checkbox state management using BooleanField

Filtering using query parameters

Debugging real Django issues (404, migrations, routing)

Improving UI with pure CSS

👨‍💻 Author

Manidhar Saggam
Python Developer (Fresher)

GitHub: https://github.com/Manidharsaggam

LinkedIn: (add your LinkedIn link)

📌 Future Improvements

User authentication

AJAX-based updates

Task priorities & deadlines

Deployment on cloud platform

⭐ If you like this project, feel free to star the repository!

---

## 🎯 Final Verdict
✅ **Correct**  
✅ **Professional**  
✅ **GitHub-ready**  
✅ **Interview-friendly**

You can confidently push this to GitHub now 💪

If you want next:
- Resume final check
- Deployment guide
- Interview Q&A based on this project

Just tell me 👍
