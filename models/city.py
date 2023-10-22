#!/usr/bin/python3

""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', cascade="all, delete-orphan", backref='cities')
    else:
        state_id = ""
        name = ""
