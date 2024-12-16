from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session, create_engine, SQLModel

SQLITE_DATABASE_URL = 'sqlite:///./inventory_starships.db'

engine = create_engine(SQLITE_DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session

def create_tables(app: FastAPI):
    #SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine, checkfirst=True)
    yield

SessionDep = Annotated[Session, Depends(get_session)]
