#!/user/bin/env python3.8
from sqlalchemy import create_engine

import os


try:
    user_name = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    engine = create_engine(
        f"postgresql://{user_name}:{password}@psql-server:5432/postgres",
        client_encoding="utf8"
    )
    with engine.connect() as conn:
        conn.execute("commit")
        conn.execute("create database corona")

    from models.database import init_db
    init_db()
except:
    pass

from models.update import update_database
update_database()
