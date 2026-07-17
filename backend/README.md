# 🐍 SkillExa

> A modern Python Learning Platform built with **FastAPI**, designed to provide interactive learning, quizzes, progress tracking, and mastery-based education.

---

# 📖 About

SkillExa is an educational platform that helps students learn Python through structured lessons, interactive quizzes, coding practice, and progress tracking.

The project now uses a single backend application with **FastAPI**. The backend serves both the API routes and the HTML pages through Jinja2 templates and static assets.

---

# ✨ Features

- 📘 Structured Python Learning
- 📝 Interactive Quizzes
- 💻 Practice Programs
- 📊 Progress Tracking
- 🔓 Topic Unlock System
- 🏆 XP & Daily Streak
- 📈 Mastery Tests
- 🎯 Beginner Friendly UI
- ⚡ FastAPI REST API
- 📱 Responsive Design

---

# 🛠 Tech Stack

### Backend

- FastAPI
- Python
- Pydantic
- Uvicorn

### Presentation Layer

- Jinja2 Templates
- HTML5
- CSS3
- JavaScript

### Database (Current)

- In-Memory Storage

### Future Database

- SQLite
- PostgreSQL

---

# 📂 Project Structure

```
SkillExa/
│
└── backend/
    │
    ├── app/
    │   ├── main.py                 # FastAPI Entry Point
    │   │
    │   ├── routes/                 # API Routes
    │   ├── models/                 # Database Models
    │   ├── schemas/                # Pydantic Schemas
    │   ├── services/               # Business Logic
    │   ├── database/               # Database Connection
    │   ├── utils/                  # Helper Functions
    │   │
    │   ├── templates/              # HTML Templates
    │   │   ├── index.html
    │   │   ├── dashboard.html
    │   │   ├── topics.html
    │   │   ├── lesson.html
    │   │   ├── quiz.html
    │   │   └── progress.html
    │   │
    │   └── static/
    │       ├── css/
    │       ├── js/
    │       └── images/
    │
    ├── requirements.txt
    ├── README.md
    └── venv/
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/SkillExa.git
```

---

## Navigate

```bash
cd SkillExa/backend
```

---

## Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv venv
```

### Windows

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Server

```bash
uvicorn app.main:app --reload
```

---

Open in your browser:

```
http://127.0.0.1:8000
```

---

# 📚 Learning Modules

- Introduction
- Variables
- Data Types
- Type Casting
- Input & Output
- Operators
- Conditional Statements
- Loops
- Functions
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
- File Handling
- Exception Handling
- Modules
- Object-Oriented Programming
- NumPy
- Final Assessment

---

# 🌐 API Endpoints

## Home / Dashboard

```
GET /
```

Renders the dashboard page.

---

## Dashboard Page

```
GET /dashboard
```

Renders the dashboard page.

---

## Python Topics

```
GET /python/topics
```

Returns all Python learning topics.

---

## Topic Details

```
GET /python/topics/{topic_id}
```

Returns the full content for a single topic.

---

## User Progress

```
GET /user/limits
```

Returns:

- XP
- Daily Quiz Count
- Streak
- Free Quiz Limit

---

## Submit Quiz

```
POST /quiz/submit
```

Example Request

```json
{
    "topic_id": 1,
    "selected_option": "A",
    "time_remaining": 40
}
```

---

# 📁 Current Frontend Location

All frontend assets now live inside the backend application:

- Templates: `backend/app/templates/`
- Stylesheets: `backend/app/static/css/`
- JavaScript: `backend/app/static/js/`
- Images: `backend/app/static/images/`

# 🏆 Future Features

- User Authentication
- JWT Login
- SQLite Database
- PostgreSQL Support
- Leaderboard
- Certificates
- AI Coding Assistant
- AI Quiz Generator
- Daily Challenges
- Coding Playground
- Code Execution
- Resume Builder
- Mock Interviews
- Dark Mode
- Admin Dashboard

---

# 📈 Development Roadmap

- [x] FastAPI Backend
- [x] REST APIs
- [x] Python Learning Modules
- [x] Progress Tracking
- [x] Quiz System
- [ ] Authentication
- [ ] Database Integration
- [ ] Admin Panel
- [ ] Certificate Generation
- [ ] AI Features
- [ ] Deployment

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Basavaraju R K**

Electronics & Communication Engineering

Python Backend Developer

---

# ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.