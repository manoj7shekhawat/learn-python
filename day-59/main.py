from flask import Flask, render_template, request
import requests as rq
import smtplib as smtp
import os
app = Flask(__name__)


EMAIL_ID = os.environ.get("EMAIL_ID")
PASS_WD = os.environ.get("PASS_WD")


@app.route("/")
def home():
    response = rq.get(url="https://api.npoint.io/cd4ef3cbd01b5814a64f")
    response.raise_for_status()
    blogs = response.json()['blogs']

    return render_template("index.html", blogs=blogs)


@app.route("/index.html")
def index():
    response = rq.get(url="https://api.npoint.io/cd4ef3cbd01b5814a64f")
    response.raise_for_status()
    blogs = response.json()['blogs']

    return render_template("index.html", blogs=blogs)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route('/contact', methods=['POST'])
def contact_form():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    with smtp.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ID, password=PASS_WD)
        connection.sendmail(to_addrs="manoj7shekhawat@gmail.com", from_addr=EMAIL_ID, msg=f"Subject: Contact\n\nName: {name}, Email: {email}, Phone: {phone}, Message: {message}")

    return render_template("contact.html")

@app.route("/<int:id>")
def post_details(id):

    response = rq.get(url="https://api.npoint.io/cd4ef3cbd01b5814a64f")
    response.raise_for_status()
    blogs = response.json()['blogs']

    for x in blogs:
        if int(x['id']) == id:
            blog = x

    return render_template("post.html", blog=blog)


if __name__ == '__main__':
    app.run(debug=True)