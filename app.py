from flask import Flask


app = Flask(__name__)


@app.route("/mnist")
def mnist():
    return "Hello World!"
