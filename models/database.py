from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


user_name = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
engine = create_engine(
    f"postgresql://{user_name}:{password}@psql-server:5432/corona",
    client_encoding="utf8"
)
db_session = scoped_session(
    sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)
