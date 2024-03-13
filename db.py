from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model.problem import Base, Problem

engine = create_engine('sqlite://')
sess = Session(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def get_problems():
    return sess.query(Problem).all()

def add_new(data):
    name = data.get('name')
    difficulty = data.get('difficulty')
    date = data.get('date')
    new_prob = Problem(name=name, difficulty=difficulty, date=date)
    sess.add(new_prob)
    sess.commit()