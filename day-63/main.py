from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)



all_books = []


class BookForm(FlaskForm):
    title = StringField(label="Book Name")
    author = StringField(label="Book Author")
    rating = IntegerField(label="Rating")
    add_book = SubmitField(label="Add Book")


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    book_form = BookForm()
    print(f"{book_form.title.data}::{book_form.author.data}::{book_form.rating.data}")
    my_dict = {
        "title": book_form.title.data,
        "author": book_form.author.data,
        "rating": book_form.rating.data
    }
    if book_form.title.data:
        all_books.append(my_dict)
    return render_template("add.html", form=book_form)


if __name__ == "__main__":
    app.run(debug=True)

