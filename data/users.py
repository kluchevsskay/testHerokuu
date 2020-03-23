from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"


if __name__ == '__main__':
    app.run()