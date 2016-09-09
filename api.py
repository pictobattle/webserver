from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/user/logIn/callback/")
def login_callback():
    return str(request.data)
