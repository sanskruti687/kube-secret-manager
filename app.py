from flask import Flask, render_template, request
from database import connect_db

app = Flask(__name__)

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

    # Save to MySQL
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO applicants (full_name, email, domain, college_name, department) VALUES (%s, %s, %s, %s, %s)",
        (full_name, email, domain, college_name, department),
    )
    conn.commit()
    conn.close()

    return "success"

if __name__ == "__main__":
    app.run(debug=True)
