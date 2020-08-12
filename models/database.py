from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models.auth_data import get_user_pass


def connect_db(user_name: str, password: str, db: str):
    engine = create_engine(
        f"postgresql://{user_name}:{password}@psql-server:5432/{db}",
        client_encoding="utf8"
    )
    db_session = scoped_session(
        sessionmaker(
            autocommit=False, autoflush=False, bind=engine
        )
    )
    Base = declarative_base()
    Base.query = db_session.query_property()
    return engine, db_session, Base, Base.query


def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)


user_name, password = get_user_pass()
try:
    engine, db_session, Base, Base.query = connect_db(
        user_name, password, "corona"
    )
except:
    engine, db_session, Base, Base.query = connect_db(
        user_name, password, "postgres"
    )
    conn = engine.connect()
    conn.excute("commit")
    conn.excute("create database corona")
    conn.close()
    engine, db_session, Base, Base.query = connect_db(
        user_name, password, "corona"
    )
    init_db()
    from models.update import update_database
    update_database()
