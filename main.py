from flask import Flask

app = Flask(__name__)


@app.route("/hi", methods=["GET"])
def say_hi():
    return "Привет"


if __name__ == "__main__":
    app.run(debug=True)
