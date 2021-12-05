import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
   )

Base = declarative_base()


class Promo(Base):
    __tablename__ = 'promo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(512), unique=True, nullable=False)
    url = Column(String(512), unique=True, nullable=False)
    add_date = Column(DateTime, unique=False, nullable=True)


    def __str__(self):
        print(self.name)

    def add(self):
        pass

