from flask import Flask

app = Flask(__name__)


@app.route("/hi", methods=["GET"])
def say_hi():
    return "Привет"


@app.route("/bye", methods=["GET"])
def say_bye():
    return "Пока."


if __name__ == "__main__":
    app.run(debug=True)
