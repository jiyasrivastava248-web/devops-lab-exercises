
from flask import Flask, jsonify, request
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Big Sale!",
        "pod": os.environ.get("HOSTNAME", "unknown"),
        "ts": time.time()
    })

@app.route("/buy")
def buy():
    return jsonify({
        "message": "Purchase request received",
        "user": request.args.get("user", "guest"),
        "pod": os.environ.get("HOSTNAME", "unknown")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
