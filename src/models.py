import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    userName = Column(String(30), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birthYear = Column(String(25), nullable=False)
    gender = Column(String(25), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    skinColor = Column(String(25), nullable=False)
    eyeColor = Column(String(25), nullable=False)
    hairColor = Column(String(25), nullable=False)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(String(25), nullable=False)
    terrain = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    surfaceWater = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    rotationPeriod = Column(Integer, nullable=True)
    orbitalPeriod = Column(Integer, nullable=True)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(80), nullable=False)
    vehicleClass = Column(String(50), nullable=False)
    passengers = Column(Integer, nullable=False)
    costInCredits = Column(Integer, nullable=False)
    maxAtmospheringSpeed = Column(Integer, nullable=False)
    length = Column(Float, nullable=False)
    crew = Column(Integer, nullable=False)
    cargoCapacity = Column(Integer, nullable=False)
    consumables = Column(String(50), nullable=False)


class FavCharacter(Base):
    __tablename__ = 'favcharacter'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))
    characterId = Column(Integer, ForeignKey('character.id'))


class FavPlanet(Base):
    __tablename__ = 'favplanet'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))
    planetId = Column(Integer, ForeignKey('planet.id'))


class FavVehicle(Base):
    __tablename__ = 'favvehicle'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))
    vehicleId = Column(Integer, ForeignKey('vehicle.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')