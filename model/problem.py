from sqlalchemy import Column, Integer, String
from db import Base

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True)
    name= Column(String(50), unique=True)
    difficulty= Column(String(10))
    date= Column(String(20))
    
    def __init__(self, name=None, difficulty=None, date=None):
        self.name = name
        self.difficulty = difficulty
        self.date = date

    def __repr__(self):
        return f'<Problem {self.name!r}>'