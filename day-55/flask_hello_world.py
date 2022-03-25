from flask import Flask

app = Flask(__name__)


def bold_decorator(function):
    def warapper_function():
        my_str = function()
        return f"<b>{my_str}</b>"

    return warapper_function


def em_decorator(function):
    def warapper_function():
        my_str = function()
        return f"<em>{my_str}</em>"

    return warapper_function


def under_decorator(function):
    def warapper_function():
        my_str = function()
        return f"<u>{my_str}</u>"

    return warapper_function

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@bold_decorator
@under_decorator
@em_decorator
def bye():
    return "Bye!!"


if __name__ == '__main__':
    app.run(debug=True)
