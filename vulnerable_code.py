from flask import Flask, request

app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    
    # 🚩 VULNERABILITY 1: SQL Injection (Direct string formatting)
    query = f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'"
    
    # 🚩 VULNERABILITY 2: XSS (Reflecting user input without escaping)
    return f"<h1>Welcome {username}</h1>" 

if __name__ == "__main__":
    app.run()