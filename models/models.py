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
        return "<Title %r>" % (self.gender)
