from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Todo(Base):
    def __init__(self, id=None, task=None, description=None, endDate=None):
        self.id = id
        self.task = task
        self.description = description
        self.endDate = endDate

    __tablename__ = 'Todo'
    id = Column(String, primary_key=True)
    task = Column(String, unique=False, nullable=True, primary_key=False)
    description = Column(String, unique=False, nullable=True, primary_key=False)
    endDate = Column(String, unique=False, nullable=True, primary_key=False)
