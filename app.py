
from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return "✅ Flask app deployed via GitHub Actions SSH"

if name == "main":
    app.run(host="0.0.0.0", port=5000)
