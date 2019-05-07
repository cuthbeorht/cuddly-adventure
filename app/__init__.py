from flask import Flask

app = Flask(__name__)

from app.users import user

@app.route('/')
def hello_world():
    return 'Hello World!'