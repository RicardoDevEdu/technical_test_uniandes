from dataclasses import dataclass
from sqlmodel import SQLModel, Field

class StarshipModel(SQLModel, table=True):
    __tablename__ = 'starships'

    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    model: str = Field(default=None)
    cost: str = Field(default=None)
    velocity: str = Field(default=None)
    load_capacity: str = Field(default=None)
    passengers: str = Field(default=None)


@dataclass
class StarShip:
    name: str
    model: str
    cost: str
    velocity: str
    load_capacity: str
    passengers: str