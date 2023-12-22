#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")

    def __str__(self):
        """String representation of a City"""
        return "{}: ({}) {}".format(self.state.name, self.id, self.name)
