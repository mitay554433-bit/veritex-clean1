from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "VERITEX LIVE"

@app.route("/health")
def health():
    return {"status": "ok"}
