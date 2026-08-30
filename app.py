from flask import Flask, request, render_template
from database import init_db, get_db

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Exam Guard"


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        with get_db() as connection:
            connection.execute(
                """
                INSERT INTO candidates (name, email, password)
                VALUES (?, ?, ?)
                """,
                (name, email, password),
            )
            connection.commit()

        return "registration successful"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        with get_db() as connection:
            candidate = connection.execute(
                """
                SELECT *
                FROM candidates
                WHERE email = ? AND password = ?
                """,
                (email, password),
            ).fetchone()

        if candidate:
            return "Login successful!"

        return "Invalid email or password"

    return render_template("login.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True, use_reloader=False)