from openpyxl import load_workbook
import requests

import datetime
import pathlib

from models.database import db_session, init_db
from models.models import corona_data


def update_database():
    url = (
        "http://www.pref.osaka.lg.jp/"
        "attach/23711/00346644/youseisyajyouhou.xlsx"
    )
    download_file = requests.get(url)
    path = pathlib.Path(__file__).joinpath(
        "..", "..", "tmp", "corona.xlsx"
    ).resolve()
    with path.open(mode="wb") as f:
        f.write(download_file.content)
    wb = load_workbook(filename=str(path), data_only=True)
    ws = wb.get_sheet_by_name("Sheet1")
    r_list = []
    for r in range(3, ws.max_row + 1):
        r_tpl = ()
        for c in range(3, ws.max_column):
            value = ws.cell(r, c).value
            if isinstance(value, datetime.datetime):
                value = value.date()
            r_tpl += (value, )
        r_list.append(r_tpl)
    items = []
    init_db()
    for i in range(0, ws.max_row - 2):
        data = corona_data()
        data.age = r_list[i][0]
        data.gender = r_list[i][1]
        data.place = r_list[i][2]
        data.date_of_onset = r_list[i][3]
        data.symptoms = r_list[i][4]
        data.hospitalization = r_list[i][5]
        items.append(data)
    db_session.add_all(items)
    db_session.commit()
