from flask import Flask, render_template
import requests as rq

app = Flask(__name__)


@app.route('/')
def home():
    response = rq.get(url="https://api.npoint.io/cd4ef3cbd01b5814a64f")
    response.raise_for_status()
    blogs = response.json()['blogs']

    return render_template("index.html", blogs=blogs)


@app.route("/post/<int:id>")
def post_details(id):

    response = rq.get(url="https://api.npoint.io/cd4ef3cbd01b5814a64f")
    response.raise_for_status()
    blogs = response.json()['blogs']

    for x in blogs:
        if int(x['id']) == id:
            blog = x

    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
