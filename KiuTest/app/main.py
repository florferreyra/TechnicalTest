import datetime
from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app import schemas, dto
from app.database.db import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """
       Create a new client.

       This endpoint allows you to create a new client in the database.
       If a client with the same name already exists, it raises an HTTP 400 error.

       Args:
           client: The client data to be created.
           db: The database session. Defaults to Depends(get_db).

       Returns:
           The newly created client.

       Raises:
           HTTPException: If a client with the same name already exists.
    """
    existing_client = dto.get_client_by_name(db=db, name=client.name)
    if existing_client:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Client already exists.")
    return dto.create_client(db=db, client=client)


@app.get("/clients/", response_model=list[schemas.Client])
def get_clients(client_id: Union[int, None] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
        Retrieve clients.

        This endpoint allows you to retrieve a list of clients from the database.
        You can specify a client ID to retrieve a specific client, or use pagination
        parameters to limit the number of clients returned.

        Args:
            client_id (optional): The ID of a specific client to retrieve. Defaults to None.
            skip (optional): The number of records to skip for pagination. Defaults to 0.
            limit (optional): The maximum number of records to return. Defaults to 100.
            db: The database session. Defaults to Depends(get_db).

        Returns:
            A list of clients or a specific client.
    """
    return dto.get_client(db, client_id=client_id) if client_id else dto.get_clients(db, skip=skip, limit=limit)


@app.get("/cargos/", response_model=schemas.TotalCargo)
def get_cargos(date: datetime.date, db: Session = Depends(get_db)):
    """
        Retrieve total cargo information for a specific date.

        This endpoint allows you to retrieve the total amount and number of cargos
        for a given date.

        Args:
            date: The date for which to retrieve cargo information.
            db: The database session. Defaults to Depends(get_db).

        Returns:
            The total amount and count of cargos for the specified date.
    """
    return dto.get_cargos(db, date=date)


@app.post("/cargos/", response_model=schemas.Cargo)
def create_cargo(cargo: schemas.CargoCreate, db: Session = Depends(get_db)):
    """
        Create a new cargo.

        This endpoint allows you to create a new cargo in the database.

        Args:
            cargo: The cargo data to be created.
            db: The database session. Defaults to Depends(get_db).

        Returns:
            The newly created cargo.
    """
    return dto.create_cargo(db, cargo=cargo)



