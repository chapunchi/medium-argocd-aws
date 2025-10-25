import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def health():
    return {"status": "ok"}, 200


@app.route("/print/<number>")
def add(number):
    env = os.getenv("APP_ENV", "unknown")
    return f"The value entered is: {number}, App is deployed in: {env}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)