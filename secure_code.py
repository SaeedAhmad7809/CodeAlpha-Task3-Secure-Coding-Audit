from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    # ✅ REMEDIATION 1: Use Parameterized Queries (Prevents SQL Injection)
    # cursor.execute("SELECT * FROM users WHERE user=? AND pass=?", (username, password))

    # ✅ REMEDIATION 2: Use Templates/Escaping (Prevents XSS)
    return render_template_string("<h1>Welcome {{ name }}</h1>", name=username)

if __name__ == "__main__":
    app.run()