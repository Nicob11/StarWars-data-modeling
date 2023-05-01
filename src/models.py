import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorite = Column('user_favorite', relationship(Base), Column('user_id', Integer, ForeignKey('user.id')), Column('planet_id', Integer, ForeignKey('planet.id')), Column('character_id', Integer, ForeignKey('character.id')), Column('vehicle_id', Integer, ForeignKey('vehicle.id')))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True ,nullable=False)
    password = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    favorite = Column(Integer, ForeignKey('favorite.id'))
    
    

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    capacity = Column(String(250), nullable=False)
    pilot_id = Column(Integer, ForeignKey('character.id'))




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
