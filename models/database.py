from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.update import update_database


class db():

    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password

    def connect_or_setup(self):
        try:
            self.engine = create_engine(
                f"postgresql://{self.user_name}:{self.password}@psql-server:5432/corona",
                client_encoding="utf8"
            )
            self.db_session = scoped_session(
                sessionmaker(
                    autocommit=False, autoflush=False, bind=self.engine
                )
            )
            self.Base = declarative_base()
            self.Base.query = self.db_session.query_property()
        except:
            engine = sqlalchemy.create_engine(
                f"postgresql://{self.user_name}:{self.password}@psql-server:5432/postgres",
                client_encoding="utf8"
            )
            conn = engine.connect()
            conn.excute("commit")
            conn.excute("create database corona")
            conn.close()
            self.connect_or_setup()
            self.init_db()
            update_database()

    def init_db(self):
        import models.models
        self.Base.metadata.create_all(bind=self.engine)
