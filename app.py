from flask import Flask, render_template, request, redirect, session
import mysql.connector
import bcrypt
import os
from werkzeug.utils import secure_filename
from resume_parser import extract_text
from ai_analyzer import analyze_resume
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Secret key
app.secret_key = os.getenv("SECRET_KEY")

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# MySQL Connection
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = db.cursor()

# -------------------------
# Login Page
# -------------------------
@app.route("/")
def login():
    return render_template("login.html")


# -------------------------
# Register Page
# -------------------------
@app.route("/register")
def register():
    return render_template("register.html")


# -------------------------
# Dashboard
# -------------------------
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template(
        "dashboard.html",
        name=session["user"]
    )


# -------------------------
# Upload Page
# -------------------------
@app.route("/upload")
def upload():

    if "user" not in session:
        return redirect("/")

    return render_template("upload.html")


# -------------------------
# Register User
# -------------------------
@app.route("/register_user", methods=["POST"])
def register_user():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        return "Email already registered!"

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    cursor.execute(
        "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
        (
            name,
            email,
            hashed_password.decode("utf-8")
        )
    )

    db.commit()

    return redirect("/")


# -------------------------
# Login User
# -------------------------
@app.route("/login_user", methods=["POST"])
def login_user():

    email = request.form["email"]
    password = request.form["password"]

    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    if user:

        stored_password = user[3]

        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password.encode("utf-8")
        ):

            session["user"] = user[1]

            return redirect("/dashboard")

    return "Invalid Email or Password"


# -------------------------
# Upload Resume
# -------------------------
@app.route("/upload_resume", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return "No file selected."

    file = request.files["resume"]

    if file.filename == "":
        return "Please select a PDF."

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # Extract text
    resume_text = extract_text(filepath)

    # Get job description
    job_description = request.form["job_description"]

    # Analyze with Gemini
    analysis = analyze_resume(
        resume_text,
        job_description
    )

    return render_template(
        "result.html",
        analysis=analysis
    )

# -------------------------
# Logout
# -------------------------
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/")


# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)