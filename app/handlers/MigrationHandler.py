from typing import Protocol, List

from app.models.domain import StarShip, Vehicle, Pilot, Specie, Planet


class Requester(Protocol):
    def starships(self) -> List[StarShip]: ...
    def vehicles(self) -> List[Vehicle]: ...
    def pilots(self) -> List[Pilot]: ...
    def species(self) -> List[Specie]: ...
    def planets(self) -> List[Planet]: ...

class Storer(Protocol):
    def starships(self, starships: List[StarShip]) -> None: ...
    def vehicles(self, vehicles: List[Vehicle]) -> None: ...
    def pilots(self, pilots: List[Pilot]) -> None: ...
    def species(self, species: List[Specie]) -> None: ...
    def planets(self, planets: List[Planet]) -> List[Planet]: ...

class MigrationHandler:
    requestor: Requester
    def __init__(self, requestor: Requester, storer: Storer):
        self.requestor = requestor
        self.storer = storer

    def start(self):
        starships = self.requestor.starships()
        vehicles = self.requestor.vehicles()
        pilots = self.requestor.pilots()
        species = self.requestor.species()
        planets = self.requestor.planets()

        self.storer.vehicles(vehicles)
        self.storer.species(species)
        self.storer.planets(planets)
        self.storer.pilots(pilots)
        self.storer.starships(starships)

        return {
            "message":"migration complete",
        }