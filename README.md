# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes PDF resumes against job descriptions using **Google Gemini AI**. The application extracts resume content, compares it with a given job description, and provides an ATS score, strengths, missing skills, and personalized suggestions to improve the resume.

---

## 🚀 Features

- 🔐 User Registration & Login
- 🔒 Secure Password Hashing using bcrypt
- 📄 PDF Resume Upload
- 📝 Resume Text Extraction using pdfplumber
- 🤖 AI-Powered Resume Analysis with Google Gemini AI
- 📊 ATS Score Generation
- ✅ Strength & Skill Analysis
- ❌ Missing Skills Detection
- 💡 Personalized Resume Improvement Suggestions
- 🗄️ MySQL Database Integration
- 🔑 Secure API & Database Credentials using `.env`

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Database
- MySQL

### AI
- Google Gemini AI

### Libraries
- pdfplumber
- bcrypt
- python-dotenv
- google-generativeai

### Tools
- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```
AI_Resume_Analyzer/
│
├── app.py
├── ai_analyzer.py
├── database.py
├── resume_parser.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── upload.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── uploads/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/harshtejpalleti/AI-Resume-Analyzer.git
```

### 2. Navigate to the project folder

```bash
cd AI-Resume-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=resume_analyzer

GEMINI_API_KEY=your_gemini_api_key
```

### 7. Create the MySQL Database

```sql
CREATE DATABASE resume_analyzer;
```

Import or create the required tables.

### 8. Run the application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. Register a new account or log in.
2. Upload a PDF resume.
3. Enter the target job description.
4. The application extracts text from the resume.
5. Google Gemini AI analyzes the resume against the job description.
6. The application displays:
   - ATS Score
   - Resume Strengths
   - Missing Skills
   - Resume Improvement Suggestions

---

## 📸 Screenshots

You can add screenshots here.

Example:

```
screenshots/
│
├── login.png
├── register.png
├── upload.png
└── result.png
```

---

## 🔮 Future Enhancements

- Resume Analysis History
- DOCX Resume Support
- Resume Keyword Optimization
- Download Analysis Report as PDF
- Dashboard Analytics
- Responsive UI Improvements
- Cloud Deployment

---

## 👨‍💻 Author

**Harsha Tej Palleti**

GitHub: https://github.com/harshtejpalleti

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
