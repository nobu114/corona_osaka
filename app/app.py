from flask import Flask, render_template
from models.models import corona_data


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


@app.route("/index")
def index():
    all_data = corona_data.query.all()
    place = []
    for data in all_data:
        place.append(data.place)
        # print(data.place)
        # print(type(data.place))
    print(place.count("大阪市"))
    number_of_infeted_people = {"大阪市":place.count("大阪市")}
    print(place)
    # print(type(place))
    return render_template("index.html", all_data=all_data)
