from flask import Flask
from flask import Response
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
