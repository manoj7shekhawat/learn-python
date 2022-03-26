from flask import Flask
from flask import render_template
from datetime import datetime as dt
import requests as rq

app = Flask(__name__)

@app.route("/")
def hello():
    now = dt.now()
    year = now.strftime("%Y")
    return render_template("index.html", yr=year)


@app.route("/guess/<string:name>")
def name_func(name):
    # https://api.agify.io/?name=mittal
    response = rq.get(url=f"https://api.agify.io/?name={name}")
    response.raise_for_status()
    res_body = response.json()
    p_name = str(res_body['name']).title()
    p_age = res_body['age']

    response = rq.get(url=f"https://api.genderize.io/?name={name}")
    response.raise_for_status()
    res_body = response.json()
    p_gender = res_body['gender'].title()

    now = dt.now()
    year = now.strftime("%Y")

    return render_template("index.html", yr=year, p_name=p_name, p_age=p_age, p_gender=p_gender)


if __name__ == '__main__':
    app.run(debug=True)