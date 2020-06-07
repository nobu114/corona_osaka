from flask import Flask, render_template
from sqlalchemy import desc, and_, or_

from models.models import corona_data


app = Flask(__name__)


def get_data(area):
    all_number = corona_data.query.filter(
        corona_data.place == area
    ).count()
    negative = corona_data.query.filter(
        and_(
            corona_data.place == area,
            or_(
                corona_data.symptoms == "―",
                corona_data.symptoms == "死亡"
            )
        )
    ).count()
    active = all_number - negative
    return (all_number, active)


@app.route("/")
def main():
    all_data = corona_data.query.order_by(
        corona_data.index
    ).all()
    symptoms_dict = {
        "mild_illness": corona_data.query.filter(
            corona_data.symptoms == "軽症"
        ).count(),
        "serious_illness": corona_data.query.filter(
            corona_data.symptoms == "重症"
        ).count(),
        "die": corona_data.query.filter(
            corona_data.symptoms == "死亡"
        ).count(),
        "asymptomatic": corona_data.query.filter(
            corona_data.symptoms == "無症状"
        ).count(),
        "end": corona_data.query.filter(
            corona_data.symptoms == "―"
        ).count(),
        "examine": corona_data.query.filter(
            corona_data.symptoms == "調査中"
        ).count()
    }
    total = corona_data.query.count()
    # 治った人
    """
    negative_people = corona_data.query.filter(
        corona_data.symptoms == "―"
    ).count()
    die_people = corona_data.query.filter(
        corona_data.symptoms == "死亡"
    ).count()
    """
    update = corona_data.query.order_by(
        desc(corona_data.publish_d)
    ).limit(1).first().publish_d.date()
    # 前日比
    cttpd = corona_data.query.filter(
        corona_data.publish_d == update
    ).count()
    update_str = update.strftime(
        "%Y年%m月%d日"
    )
    number_of_infeted_people = {
        "大阪市": get_data("大阪市"),
        "堺市": get_data("堺市"),
        "能勢町": get_data("能勢町"),
        "豊能町": get_data("豊能町"),
        "池田市": get_data("池田市"),
        "箕面市": get_data("箕面市"),
        "豊中市": get_data("豊中市"),
        "茨木市": get_data("茨木市"),
        "高槻市": get_data("高槻市"),
        "島本町": get_data("島本町"),
        "吹田市": get_data("吹田市"),
        "摂津市": get_data("摂津市"),
        "枚方市": get_data("枚方市"),
        "交野市": get_data("交野市"),
        "寝屋川市": get_data("寝屋川市"),
        "守口市": get_data("守口市"),
        "門真市": get_data("門真市"),
        "四條畷市": get_data("四條畷市"),
        "大東市": get_data("大東市"),
        "東大阪市": get_data("東大阪市"),
        "八尾市": get_data("八尾市"),
        "柏原市": get_data("柏原市"),
        "和泉市": get_data("和泉市"),
        "高石市": get_data("高石市"),
        "泉大津市": get_data("泉大津市"),
        "忠岡町": get_data("忠岡町"),
        "岸和田市": get_data("岸和田市"),
        "貝塚市": get_data("貝塚市"),
        "熊取町": get_data("熊取町"),
        "泉佐野市": get_data("泉佐野市"),
        "田尻町": get_data("田尻町"),
        "泉南市": get_data("泉南市"),
        "阪南市": get_data("阪南市"),
        "岬町": get_data("岬町"),
        "松原市": get_data("松原市"),
        "羽曳野市": get_data("羽曳野市"),
        "藤井寺市": get_data("藤井寺市"),
        "太子町": get_data("太子町"),
        "河南町": get_data("河南町"),
        "千早赤阪村": get_data("千早赤阪村"),
        "富田林市": get_data("富田林市"),
        "大阪狭山市": get_data("大阪狭山市"),
        "河内長野市": get_data("河内長野市")
    }
    people_dict = {
        "未就学児": corona_data.query.filter(
            corona_data.age == "未就学児"
        ).count(),
        "就学児": corona_data.query.filter(
            corona_data.age == "就学児"
        ).count(),
        "10": corona_data.query.filter(
            corona_data.age == "10"
        ).count(),
        "20": corona_data.query.filter(
            corona_data.age == "20"
        ).count(),
        "30": corona_data.query.filter(
            corona_data.age == "30"
        ).count(),
        "40": corona_data.query.filter(
            corona_data.age == "40"
        ).count(),
        "50": corona_data.query.filter(
            corona_data.age == "50"
        ).count(),
        "60": corona_data.query.filter(
            corona_data.age == "60"
        ).count(),
        "70": corona_data.query.filter(
            corona_data.age == "70"
        ).count(),
        "80": corona_data.query.filter(
            corona_data.age == "80"
        ).count(),
        "90": corona_data.query.filter(
            corona_data.age == "90"
        ).count(),
        "100": corona_data.query.filter(
            corona_data.age == "100"
        ).count()
    }

    return render_template(
        "index.html", all_data=all_data, np=number_of_infeted_people,
        total=total, date=update_str, cttpd=cttpd, people_dict=people_dict,
        symptoms_dict=symptoms_dict
    )
