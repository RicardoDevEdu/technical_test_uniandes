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
    homeworld: int

