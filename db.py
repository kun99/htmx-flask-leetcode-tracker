from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from leetcode_journal.model.problem import Problem

Base = declarative_base()
engine = create_engine('sqlite://')
sess = Session(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def get_problems():
    return sess.query(Problem).all()

def new_problem(data):
    new_prob = Problem(data)
    sess.add(new_prob)
    sess.commit()
    sess.close()