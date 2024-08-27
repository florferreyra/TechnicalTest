import datetime

from sqlalchemy import func
from sqlalchemy.orm import Session

from . import schemas
from .database import models


def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(name=client.name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def get_client_by_name(db: Session, name: str):
    return db.query(models.Client).filter(models.Client.name == name).first()


def get_client(db: Session, client_id: int):
    return [db.query(models.Client).get(client_id)]


def get_cargos(db: Session, date: datetime.date):
    cargos = db.query(
        func.count(models.Cargo.id).label('total_cargos'),
        func.sum(models.Cargo.price).label('total_price')
        ).filter(models.Cargo.date == date).first()
    return cargos


def create_cargo(db: Session, cargo: schemas.CargoCreate):
    db_cargo = models.Cargo(date=cargo.date,
                            origin=cargo.origin,
                            destination=cargo.destination,
                            client_id=cargo.client_id)
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo
