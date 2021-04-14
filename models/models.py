from sqlalchemy import (
    Column, Integer, Text, DateTime
)

from models.database import Base


class corona_data(Base):
    __tablename__ = "corona_data"
    index = Column(Integer, primary_key=True)
    publish_d = Column(DateTime)
    age = Column(Text)
    gender = Column(Text)
    place = Column(Text)
    # date_of_onset = Column(Text)
    symptoms = Column(Text)
    hospitalization = Column(Text)

    def __init__(
            self, index=index, publish_d=None, age=None, gender=None,
            place=None, date_of_onset=None, symptoms=None,
            hospitalization=None):
        self.index = index
        self.publish_d = publish_d
        self.age = age
        self.gender = gender
        self.place = place
        # self.date_of_onset = date_of_onset
        self.symptoms = symptoms
        self.hospitalization = hospitalization

    def __repr__(self):
        return f"<Index {self.index}>"
