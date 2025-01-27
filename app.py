from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db_config = {
    "host": "mysql",
    "user": "root",
    "password": "admin123",
    "database": "user_db",
}

# Route to display the registration page and user list
@app.route("/")
def index():
    # Fetch user data from the database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")  # Fetch all users
        users = cursor.fetchall()  # Get all rows from the query result
        cursor.close()
        conn.close()
    except Exception as e:
        return f"Error fetching users: {e}"

    # Pass the user data to the template
    return render_template("register.html", users=users)

# Route to handle form submission
@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]

    # Save data to MySQL
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"Error: {e}"

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

