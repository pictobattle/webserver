from flask import Flask, request
import requests
import os
app = Flask(__name__)

API_URL = "http://api.pictobattle.com"

LOGIN_CALLBACK_URI = "/user/logIn/callback/"
INSTAGRAM_ID = os.environ['INSTAGRAM_ID']
INSTAGRAM_SECRET = os.environ['INSTAGRAM_SECRET']


@app.route("/")
def index():
    return "Hello World!"


@app.route(LOGIN_CALLBACK_URI)
def login_callback():
    GRANT_TYPE = 'authorization_code'
    url_data = {'client_id': INSTAGRAM_ID, 'client_secret': INSTAGRAM_SECRET,
                'grant_type': GRANT_TYPE,
                'redirect_uri': API_URL + LOGIN_CALLBACK_URI,
                'code': request.args.get('code')}
    req = requests.post('https://api.instagram.com/oauth/access_token',
                        data=url_data)
    user_data = req.text
    return str(user_data)
