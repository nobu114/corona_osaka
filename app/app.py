from flask import Flask, render_template
from sqlalchemy import desc

from models.models import corona_data


app = Flask(__name__)


@app.route("/")
def main():
    all_data = corona_data.query.order_by(
        corona_data.index
    ).all()
    total = corona_data.query.count()
    negative_people = corona_data.query.filter(
        corona_data.symptoms == "―"
    ).count()
    die_people = corona_data.query.filter(
        corona_data.symptoms == "死亡"
    ).count()
    positivity_people = total - (die_people + negative_people)
    update = corona_data.query.order_by(
        desc(corona_data.publish_d)
    ).limit(1).first().publish_d.date()
    cttpd = corona_data.query.filter(
        corona_data.publish_d == update
    ).count()
    update_str = update.strftime(
        "%Y年%m月%d日"
    )
    number_of_infeted_people = {
        "大阪市": corona_data.query.filter(
            corona_data.place == "大阪市"
        ).count(),
        "堺市": corona_data.query.filter(
            corona_data.place == "堺市"
        ).count(),
        "能勢町": corona_data.query.filter(
            corona_data.place == "能勢町"
        ).count(),
        "豊能町": corona_data.query.filter(
            corona_data.place == "豊能町"
        ).count(),
        "池田市": corona_data.query.filter(
            corona_data.place == "池田市"
        ).count(),
        "箕面市": corona_data.query.filter(
            corona_data.place == "箕面市"
        ).count(),
        "豊中市": corona_data.query.filter(
            corona_data.place == "豊中市"
        ).count(),
        "茨木市": corona_data.query.filter(
            corona_data.place == "茨木市"
        ).count(),
        "高槻市": corona_data.query.filter(
            corona_data.place == "高槻市"
        ).count(),
        "島本町": corona_data.query.filter(
            corona_data.place == "島本町"
        ).count(),
        "吹田市": corona_data.query.filter(
            corona_data.place == "吹田市"
        ).count(),
        "摂津市": corona_data.query.filter(
            corona_data.place == "摂津市"
        ).count(),
        "枚方市": corona_data.query.filter(
            corona_data.place == "枚方市"
        ).count(),
        "交野市": corona_data.query.filter(
            corona_data.place == "交野市"
        ).count(),
        "寝屋川市": corona_data.query.filter(
            corona_data.place == "寝屋川市"
        ).count(),
        "守口市": corona_data.query.filter(
            corona_data.place == "守口市"
        ).count(),
        "門真市": corona_data.query.filter(
            corona_data.place == "門真市"
        ).count(),
        "四條畷市": corona_data.query.filter(
            corona_data.place == "四條畷市"
        ).count(),
        "大東市": corona_data.query.filter(
            corona_data.place == "大東市"
        ).count(),
        "東大阪市": corona_data.query.filter(
            corona_data.place == "東大阪市"
        ).count(),
        "八尾市": corona_data.query.filter(
            corona_data.place == "八尾市"
        ).count(),
        "柏原市": corona_data.query.filter(
            corona_data.place == "柏原市"
        ).count(),
        "和泉市": corona_data.query.filter(
            corona_data.place == "和泉市"
        ).count(),
        "高石市": corona_data.query.filter(
            corona_data.place == "高石市"
        ).count(),
        "泉大津市": corona_data.query.filter(
            corona_data.place == "泉大津市"
        ).count(),
        "忠岡町": corona_data.query.filter(
            corona_data.place == "忠岡町"
        ).count(),
        "岸和田市": corona_data.query.filter(
            corona_data.place == "岸和田市"
        ).count(),
        "貝塚市": corona_data.query.filter(
            corona_data.place == "貝塚市"
        ).count(),
        "熊取町": corona_data.query.filter(
            corona_data.place == "熊取町"
        ).count(),
        "泉佐野市": corona_data.query.filter(
            corona_data.place == "泉佐野市"
        ).count(),
        "田尻町": corona_data.query.filter(
            corona_data.place == "田尻町"
        ).count(),
        "泉南市": corona_data.query.filter(
            corona_data.place == "泉南市"
        ).count(),
        "阪南市": corona_data.query.filter(
            corona_data.place == "阪南市"
        ).count(),
        "岬町": corona_data.query.filter(
            corona_data.place == "岬町"
        ).count(),
        "松原市": corona_data.query.filter(
            corona_data.place == "松原市"
        ).count(),
        "羽曳野市": corona_data.query.filter(
            corona_data.place == "羽曳野市"
        ).count(),
        "藤井寺市": corona_data.query.filter(
            corona_data.place == "藤井寺市"
        ).count(),
        "太子町": corona_data.query.filter(
            corona_data.place == "太子町"
        ).count(),
        "河南町": corona_data.query.filter(
            corona_data.place == "河南町"
        ).count(),
        "千早赤阪村": corona_data.query.filter(
            corona_data.place == "千早赤阪村"
        ).count(),
        "富田林市": corona_data.query.filter(
            corona_data.place == "富田林市"
        ).count(),
        "大阪狭山市": corona_data.query.filter(
            corona_data.place == "大阪狭山市"
        ).count(),
        "河内長野市": corona_data.query.filter(
            corona_data.place == "河内長野市"
        ).count()
    }
    return render_template(
        "index.html", all_data=all_data, np=number_of_infeted_people,
        total=total, positivity_people=positivity_people,
        date=update_str, cttpd=cttpd, die_people=die_people
    )
