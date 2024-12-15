from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Pilot:
    name: str
    height: str
    mass: str
    gender: str
    birth_year: str
    species: List[int]
    vehicles: List[int]
    planet: int
    id: Optional[int] = None


@dataclass
class Planet:
    name: str
    id: Optional[int] = None


@dataclass
class Specie:
    name: str
    id: Optional[int] = None


@dataclass
class StarShip:
    name: str
    model: str
    cost: str
    velocity: str
    load_capacity: str
    passengers: str
    pilots: List[int]
    id: Optional[int] = None


@dataclass
class Vehicle:
    name: str
    id: Optional[int] = None
