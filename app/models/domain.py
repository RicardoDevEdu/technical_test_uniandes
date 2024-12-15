from dataclasses import dataclass
from typing import List

@dataclass
class Pilot:
    id:int
    name: str
    height: str
    mass: str
    gender: str
    birth_year: str
    species: List[int]
    vehicles: List[int]
    planet: int


@dataclass
class Planet:
    id: int
    name: str


@dataclass
class Specie:
    id:int
    name: str


@dataclass
class StarShip:
    name: str
    model: str
    cost: str
    velocity: str
    load_capacity: str
    passengers: str
    pilots: List[int]


@dataclass
class Vehicle:
    id: int
    name: str
