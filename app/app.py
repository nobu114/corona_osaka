from flask import Flask, render_template
from models.models import corona_data


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


@app.route("/index")
def index():
    all_data = corona_data.query.all()
    for data in all_data:
        print(data.place)
        print(type(data.place))
    # print(place)
    # print(type(place))
    return render_template("index.html", all_data=all_data)
