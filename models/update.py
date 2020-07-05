# -*- coding: utf-8 -*-

from openpyxl import load_workbook
import requests
# from sqlalchemy.dialects.postgresql import insert

import datetime
import pathlib
import zipfile

"""
from models.database import engine
from models.models import corona_data
"""


def update_database():
    url = (
        "https://github.com/codeforosaka/covid19/archive/master.zip"
    )
    download_file = requests.get(url)
    # ファイルを保存するパスの指定と存在確認
    path = pathlib.Path(__file__).joinpath(
        "..", "..", "tmp"
    ).resolve()
    if path.exists() is False:
        path.mkdir()
    path = path.joinpath("corona.zip")
    with path.open(mode="wb") as f:
        f.write(download_file.content)
    with zipfile.ZipFile(path) as existing_zip:
        existing_zip.extractall(path.joinpath("..", "data"))
    wb = load_workbook(filename=str(path.joinpath(
        "..", "data", "covid19-master", 
    )), data_only=True)
    ws = wb.get_sheet_by_name("Sheet1")
    r_list = []
    for r in range(3, ws.max_row + 1):
        r_tpl = ()
        for c in range(1, ws.max_column):
            value = ws.cell(r, c).value
            if c == 2:
                value = datetime.date(
                    year=1900, month=1, day=1
                ) + datetime.timedelta(days=value - 2)
            if isinstance(value, datetime.datetime):
                value = value.date()
            r_tpl += (value, )
        r_list.append(r_tpl)
    insert_stmt = insert(corona_data)
    set_ = dict(
        index=insert_stmt.excluded.index,
        publish_d=insert_stmt.excluded.publish_d,
        age=insert_stmt.excluded.age,
        gender=insert_stmt.excluded.gender,
        place=insert_stmt.excluded.place,
        date_of_onset=insert_stmt.excluded.date_of_onset,
        symptoms=insert_stmt.excluded.symptoms
        # hospitalization=insert_stmt.excluded.hospitalization
    )
    insert_stmt = insert_stmt.on_conflict_do_update(
        index_elements=["index"], set_=set_
    )
    with engine.connect() as conn:
        values = []
        for i in range(0, ws.max_row - 2):
            data = {}
            data["index"] = r_list[i][0]
            data["publish_d"] = r_list[i][1]
            data["age"] = r_list[i][2]
            data["gender"] = r_list[i][3]
            data["place"] = r_list[i][4]
            data["date_of_onset"] = r_list[i][5]
            data["symptoms"] = r_list[i][6]
            # data["hospitalization"] = r_list[i][7]
            values.append(data)
        conn.execute(insert_stmt, values)


if __name__ == "__main__":
    update_database()
