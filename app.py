from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test_route():
    return("<p>Hello World</p>")