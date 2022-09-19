from flask import Flask

app = Flask(__name__)


@app.route("/home", method=["GET", "POST"])
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
