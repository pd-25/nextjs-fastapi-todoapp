from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.config import databaseconfig
from typing import Generator

SQLALCHEMY_DATABASE_URL = databaseconfig.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db() -> Generator:
    db = SESSIONLOCAL()
    try:
        yield db
    finally:
        db.close()
