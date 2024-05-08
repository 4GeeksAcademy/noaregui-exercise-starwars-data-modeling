import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(200), unique=True)
    firstname = Column(String(200))
    last_name = Column(String(200))
    email = Column(String(200))

    favoritos = relationship("Favoritos")

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer)
    name = Column(String(200))
    diametro = Column(Integer)
    clima = Column(String(200))

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer)
    name = Column(String(200))
    altura = Column(Integer)
    peso = Column(Integer)
    color_piel = Column(String(200))

    favoritos = relationship("favoritos")

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    vehiculo_id = Column(Integer)
    name = Column(String(200))
    velocidad = Column(Integer)
    modelo = Column(String(200))
    color = Column(String(200))

    favoritos = relationship("favoritos")
   
class Favoritos(Base):
    __tablename__ = 'favoritos'
    favorito_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.user_id"))
    personaje_id = Column(Integer, ForeignKey("personajes.personaje_id"))
    planeta_id = Column(Integer, ForeignKey("planetas.planeta_id"))
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.vehiculos_id"))

    # Relación con Usuario (muchos a uno)
    usuario = relationship("Usuario")

    # Relación con Personajes (muchos a uno)
    personajes = relationship("Personajes")

    # Relación con Planetas (muchos a uno)
    planetas = relationship("Planetas")

    vehiculos = relationship("Vehiculos")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
