from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, TIMESTAMP, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declaratice_base()

class User(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, sever_default=func.now())
    interated_at = Column(TIMESTAMP, onupdate=func.now())
    esp32_data = Column(JSON)
    
