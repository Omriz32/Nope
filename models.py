from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()

# TODO: Add your models below this line!

class User(Base):
  
  #give a name to the table
  __tablename__ = 'users'

  #create columns (properties)
  id = Column(Integer, primary_key = True)
  name = Column(String)
  email = Column(String)
  password = Column(String)


# class Log(Base):
  
#   #give a name to the table
#   __tablename__ = 'logs'

#   #create columns (properties)
#   id = Column(Integer, primary_key = True)
#   email = Column(String)
#   password = Column(Integer)
