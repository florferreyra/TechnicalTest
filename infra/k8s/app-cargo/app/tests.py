import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.db import Base
from app.main import app, get_db

# Create a temporary database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


# Override the get_db dependency to use the testing database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# Test creating a new client
def test_create_client(db_session):
    response = client.post(
        "/clients/",
        json={"name": "Test Client"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Client"
    assert "id" in data


# Test getting clients
def test_get_clients(db_session):
    response = client.get("/clients/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


# Test creating a new cargo
def test_create_cargo(db_session):
    response = client.post(
        "/cargos/",
        json={"client_id": 1,
              "origin": "Cordoba",
              "destination": "Buenos Aires",
              "date": "2024-06-18"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["client_id"] == 1
    assert data["price"] == 10.0
    assert data["origin"] == "Cordoba"
    assert data["destination"] == "Buenos Aires"
    assert "id" in data


# Test getting cargos for a specific date
def test_get_cargos(db_session):
    # create cargos
    response = client.post(
        "/cargos/",
        json={"client_id": 1,
              "origin": "Cordoba",
              "destination": "Buenos Aires",
              "date": "2024-06-18"}
    )
    assert response.status_code == 200

    response = client.post(
        "/cargos/",
        json={"client_id": 2,
              "origin": "Cordoba",
              "destination": "Buenos Aires",
              "date": "2024-06-18"}
    )
    assert response.status_code == 200

    date = "2024-06-18"
    response = client.get(f"/cargos/?date={date}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "total_price" in data
    assert "total_cargos" in data
    assert data["total_price"] == 20.0
    assert data["total_cargos"] == 2


if __name__ == "__main__":
    pytest.main()
