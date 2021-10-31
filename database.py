from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from models import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# TODO: Add your database functions below this line!

def add_user(name , email, password):
  user_object = User(name=name, email=email, password=password)
  session.add(user_object)
  session.commit()

def query_all():
  users= session.query(User).all()
  return users

def get_user_by_email(email):
  user = session.query(User).filter_by(email = email).first()
  return user