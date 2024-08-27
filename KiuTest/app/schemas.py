import datetime
from typing import List

from pydantic import BaseModel


class ClientCreate(BaseModel):
    name: str


class Cargo(BaseModel):
    id: int
    date: datetime.date
    client_id: int
    price: float
    origin: str
    destination: str


class Client(BaseModel):
    id: int
    name: str
    cargos: List[Cargo]


class CargoCreate(BaseModel):
    client_id: int
    origin: str
    destination: str
    date: datetime.date


class TotalCargo(BaseModel):
    total_price: float
    total_cargos: int