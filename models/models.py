from sqlalchemy import (
    Column, Integer, String, Text, DateTime
)
from models.database import Base
from datetime import datetime


class corona_data(Base):
    __tablename__ = "corona_data"
    id = Column(Integer, primary_key=True)
    gender = Column(Text)
    age = Column(Text)
    place = Column(Text)
    date_of_onset = Column(DateTime)
    fever = Column(Integer)
    cough = Column(Integer)
    sputum = Column(Integer)
    nasal_discharge = Column(Integer)
    headache = Column(Integer)
    sore_throat = Column(Integer)
    dyspnea = Column(Integer)
    lethargy = Column(Integer)
    taste_disorder = Column(Integer)
    olfactory_impairment = Column(Integer)
    pneumonia = Column(Integer)
    asymptomatic = Column(Integer)

    def __init__(
            self, gender=None, age=None, place=None, date_of_onset=None,
            fever=None, cough=None, sputum=None, nasal_discharge=None,
            headache=None, sore_throat=None, dyspnea=None, lethargy=None,
            taste_disorder=None, olfactory_impairment=None, pneumonia=None,
            asymptomatic=None):
        self.gender = gender
        self.age = age
        self.place = place
        self.date_of_onset = date_of_onset
        self.fever = fever
        self.cough = cough
        self.sputum = sputum
        self.nasal_discharge = nasal_discharge
        self.headache = headache
        self.sore_throat = sore_throat
        self.dyspnea = dyspnea
        self.lethargy = lethargy
        self.taste_disorder = taste_disorder
        self.olfactory_impairment = olfactory_impairment
        self.pneumonia = pneumonia
        self.asymptomatic = asymptomatic

    def __repr__(self):
        return "<Title %r>" % (self.id)
