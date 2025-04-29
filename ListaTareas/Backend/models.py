from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tarea(Base):
    __tablename__ ='Tareas'

    id=Column(Integer, primary_key=True, index= True)
    name = Column(String(75), index=True)
    done = Column(Boolean, unique=False, default=True)
