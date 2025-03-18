from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
from database import connect_db

app = Flask(__name__)
UPLOAD_FOLDER = "uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    full_name = request.form["full_name"]
    email = request.form["email"]
    domain = request.form["domain"]
    college_name = request.form["college_name"]
    department = request.form["department"]
    resume = request.files["resume"]

    # Save Resume File
    resume_filename = secure_filename(resume.filename)
    resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_filename)
    resume.save(resume_path)

    # Save to MySQL
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO applicants (full_name, email, domain, college_name, department, resume) VALUES (%s, %s, %s, %s, %s, %s)",
        (full_name, email, domain, college_name, department, resume_filename),
    )
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
