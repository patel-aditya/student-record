from sqlalchemy import Column, Integer, String
from database import Base

class StudentInfo(Base):
    __tablename__ = "students-info"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)
    year = Column(String)
    email = Column(String)