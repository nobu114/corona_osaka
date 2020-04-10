from flask import Flask, render_template
from sqlalchemy import desc

from models.models import corona_data

# import datetime


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


@app.route("/index")
def index():
    all_data = corona_data.query.all()
    latest_pd = corona_data.query.order_by(
        desc(corona_data.publish_d)
    ).limit(1)
    for pd in latest_pd:
        hoge = pd.publish_d.date().strftime(
            "%Y年%m月%d日"
        )
        # print(hoge)
    index = []
    publish_d = []
    age = []
    gender = []
    place = []
    date_of_onset = []
    symptoms = []
    hospitalization = []
    for data in all_data:
        index.append(data.index)
        publish_d.append(data.publish_d)
        age.append(data.age)
        gender.append(data.gender)
        place.append(data.place)
        date_of_onset.append(data.date_of_onset)
        symptoms.append(data.symptoms)
        hospitalization.append(data.hospitalization)
    hospitalization_dict = {
        "入院中": hospitalization.count("入院中"),
        "入院調整中": hospitalization.count("入院調整中"),
        "退院": hospitalization.count("退院"),
        "死亡退院": hospitalization.count("死亡退院")
    }
    number_of_infeted_people = {
        "大阪市": place.count("大阪市"), "堺市": place.count("堺市"),
        "能勢町": place.count("能勢町"), "豊能町": place.count("豊能町"),
        "池田市": place.count("池田市"), "箕面市": place.count("箕面市"),
        "豊中市": place.count("豊中市"), "茨木市": place.count("茨木市"),
        "高槻市": place.count("高槻市"), "島本町": place.count("島本町"),
        "吹田市": place.count("吹田町"), "摂津市": place.count("摂津市"),
        "枚方市": place.count("枚方市"), "交野市": place.count("交野市"),
        "寝屋川市": place.count("寝屋川市"), "守口市": place.count("守口市"),
        "門真市": place.count("門真市"), "四條畷市": place.count("四條畷市"),
        "大東市": place.count("大東市"), "東大阪市": place.count("東大阪市"),
        "八尾市": place.count("八尾市"), "柏原市": place.count("柏原市"),
        "和泉市": place.count("和泉市"), "高石市": place.count("高石市"),
        "泉大津市": place.count("泉大津市"), "忠岡町": place.count("忠岡町"),
        "岸和田市": place.count("岸和田市"), "貝塚市": place.count("貝塚市"),
        "熊取町": place.count("熊取町"), "泉佐野市": place.count("泉佐野市"),
        "田尻町": place.count("田尻町"), "泉南市": place.count("泉南市"),
        "阪南市": place.count("阪南市"), "岬町": place.count("岬町"),
        "松原市": place.count("松原市"), "羽曳野市": place.count("羽曳野市"),
        "藤井寺市": place.count("藤井寺市"), "太子町": place.count("太子町"),
        "河南町": place.count("河南町"), "千早赤阪村": place.count("千早赤阪村"),
        "富田林市": place.count("富田林市"), "大阪狭山市": place.count("大阪狭山市"),
        "河内長野市": place.count("河内長野市")
    }
    total = len(index)
    positivity_pepople = (hospitalization_dict["入院中"]
                          + hospitalization_dict["入院調整中"])
    print(hoge)
    # print(type(hoge[0]))
    return render_template(
        "index.html", all_data=all_data, np=number_of_infeted_people,
        total=total, positivity_pepople=positivity_pepople,
        date=hoge
    )
