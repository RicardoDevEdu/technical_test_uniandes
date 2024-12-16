from dataclasses import dataclass
from typing import List, Optional, Dict

from app.models.database import SpecieModel, VehicleModel, PlanetModel


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
class PilotResult(Pilot):
    species: List[SpecieModel]
    vehicles: List[VehicleModel]
    planet: PlanetModel

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
    pilots: Optional[List[int]] = None
    id: Optional[int] = None


@dataclass
class Vehicle:
    name: str
    id: Optional[int] = None
