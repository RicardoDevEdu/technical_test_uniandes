from typing import Protocol, List

from app.models.domain import StarShip


class StarShipStorer(Protocol):
    def get_all_starships(self) -> List[StarShip]: ...
    def get_starship(self, id: int) -> StarShip: ...
    def update_starship(self, id: int, starship: StarShip) -> StarShip: ...

class StarshipHandler:
    def __init__(self, storage: StarShipStorer):
        self.storage = storage

    def get_all(self):
        return self.storage.get_all_starships()


    def get_starship(self, id: int) -> StarShip:
        return self.storage.get_starship(id)

    def update_starship(self, id: int, starship: StarShip) -> StarShip:
        return self.storage.update_starship(id, starship)