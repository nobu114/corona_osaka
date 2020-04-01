from models.database import db_session
from models.models import corona_data
import datetime

c1 = corona_data("女性","40代","大阪市",datetime.datetime(year=2020,month=1,day=20),1,1.0,1,0,1,0,0,0,0,1,0)
db_session.add(c1)
db_session.commit()