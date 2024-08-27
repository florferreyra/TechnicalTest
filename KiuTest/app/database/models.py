from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .db import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    cargos = relationship("Cargo", back_populates="client")


class Cargo(Base):
    __tablename__ = "cargos"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    price = Column(Float, default=10)
    origin = Column(String)
    destination = Column(String)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="cargos")





