 
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "internships.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            application_date TEXT NOT NULL,
            status TEXT NOT NULL,
            link TEXT
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
 
@app.route("/")
def home():
    conn = get_db_connection()

    applications = conn.execute(
        "SELECT * FROM applications ORDER BY id DESC"
    ).fetchall()

    total = conn.execute(
        "SELECT COUNT(*) FROM applications"
    ).fetchone()[0]

    applied = conn.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Applied'"
    ).fetchone()[0]

    interview = conn.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Interview'"
    ).fetchone()[0]

    rejected = conn.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Rejected'"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        applications=applications,
        total=total,
        applied=applied,
        interview=interview,
        rejected=rejected
    )


@app.route("/add", methods=["POST"])
def add_application():
    company = request.form["company"].strip()
    role = request.form["role"].strip()
    application_date = request.form["date"]
    status = request.form["status"]
    link = request.form.get("link", "").strip()

    if not company or not role or not application_date:
        return "Company, role, and date are required.", 400

    conn = get_db_connection()
    conn.execute("""
        INSERT INTO applications
        (company, role, application_date, status, link)
        VALUES (?, ?, ?, ?, ?)
    """, (company, role, application_date, status, link))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))


@app.route("/delete/<int:application_id>", methods=["POST"])
def delete_application(application_id):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM applications WHERE id = ?",
        (application_id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
