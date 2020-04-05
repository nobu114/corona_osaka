from sqlalchemy import (
    Column, Integer, Text
)
from models.database import Base


class corona_data(Base):
    __tablename__ = "corona_data"
    index = Column(Integer, primary_key=True)
    gender = Column(Text)
    age = Column(Text)
    place = Column(Text)
    date_of_onset = Column(Text)
    fever = Column(Text)
    cough = Column(Text)
    sputum = Column(Text)
    nasal_discharge = Column(Text)
    headache = Column(Text)
    sore_throat = Column(Text)
    dyspnea = Column(Text)
    lethargy = Column(Text)
    taste_disorder = Column(Text)
    olfactory_impairment = Column(Text)
    pneumonia = Column(Text)
    asymptomatic = Column(Text)

    def __repr__(self):
        return f"<Index {self.index}>"
