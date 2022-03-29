from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, IntegerField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/new-books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=True, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()


class BookForm(FlaskForm):
    title = StringField(label="Book Name")
    author = StringField(label="Book Author")
    rating = IntegerField(label="Rating")
    add_book = SubmitField(label="Add Book")


@app.route('/')
def home():
    all_books = Book.query.all()
    print(f"{all_books}")
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    book_form = BookForm()
    print(f"{book_form.title.data}::{book_form.author.data}::{book_form.rating.data}")

    if book_form.title.data:
        book = Book(title=book_form.title.data, author=book_form.author.data, rating=book_form.rating.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=book_form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

