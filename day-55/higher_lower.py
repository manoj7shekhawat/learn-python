import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/JdFEeta1hLNnO/giphy.gif'>"


@app.route("/<int:num>")
def number(num):
    my_num = random.randint(0, 9)
    if num == my_num:
        return "<h1 style='color:green;'>You found it</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif num < my_num:
        return "<h1 style='color:red;'>Too low, try again.</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color:blue;'>Too high, try again.</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)


