from flask import Flask, render_template
from sqlalchemy import desc, or_

from models.models import corona_data

# import datetime


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


@app.route("/index")
def index():
    all_data = corona_data.query.order_by(
        corona_data.index
    ).all()
    total = corona_data.query.count()
    positivity_pepople = corona_data.query.filter(
        or_(
            corona_data.hospitalization == "入院中",
            corona_data.hospitalization == "入院調整中"
        )
    ).count()
    update = corona_data.query.order_by(
        desc(corona_data.publish_d)
    ).limit(1).first().publish_d.date()
    # prev = update - datetime.timedelta(days=1)
    cttpd = corona_data.query.filter(
        corona_data.publish_d == update
    ).count()
    """
    prev_np = corona_data.query.filter(
        corona_data.publish_d == prev
    ).count()
    cttpd = latest_np - prev_np
    """
    update_str = update.strftime(
        "%Y年%m月%d日"
    )
    place = []
    for data in all_data:
        place.append(data.place)
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
    return render_template(
        "index.html", all_data=all_data, np=number_of_infeted_people,
        total=total, positivity_pepople=positivity_pepople,
        date=update_str, cttpd=cttpd
    )
