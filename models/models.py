from sqlalchemy import (
    Column, Integer, String, Text, DateTime
)
from models.database import Base


class corona_data(Base):
    __tablename__ = "corona_data"
    index = Column(Integer, primary_key=True)
    gender = Column(Text, nullable=True)
    age = Column(Text, nullable=True)
    place = Column(Text, nullable=True)
    date_of_onset = Column(DateTime, nullable=True)
    fever = Column(Integer, nullable=True)
    cough = Column(Integer, nullable=True)
    sputum = Column(Integer, nullable=True)
    nasal_discharge = Column(Integer, nullable=True)
    headache = Column(Integer, nullable=True)
    sore_throat = Column(Integer, nullable=True)
    dyspnea = Column(Integer, nullable=True)
    lethargy = Column(Integer, nullable=True)
    taste_disorder = Column(Integer, nullable=True)
    olfactory_impairment = Column(Integer, nullable=True)
    pneumonia = Column(Integer, nullable=True)
    asymptomatic = Column(Integer, nullable=True)

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
