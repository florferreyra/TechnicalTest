import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

secret_path = os.environ.get('HOST_CONNECTION_PATH', "/run/secrets/HOST_CONNECTION")
f = open(secret_path, "r")
SQLALCHEMY_DATABASE_URL = f.read()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
