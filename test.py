from flask import Flask
from flask import Response
import requests
app = Flask(__name__)

@app.route("/")
def proxy_example():
    r = requests.get("http://127.0.0.1:5000/")
    print(r.text)
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content-type'],
    )