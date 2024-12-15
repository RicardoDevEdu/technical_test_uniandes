from unittest.mock import MagicMock

from app.handlers.MigrationHandler import MigrationHandler, Storer, Requester
from app.models.domain import Planet, Specie, Vehicle, Pilot, StarShip


def test_migration_handler_start(monkeypatch):

    storage = MagicMock(spec=Storer)
    storage.vehicles.return_value = None
    storage.species.return_value = None
    storage.planets.return_value = None
    storage.pilots.return_value = None
    storage.starships.return_value = None


    requestor = MagicMock(spec=Requester)
    requestor.planets.return_value = [Planet(name="Tatooine")]
    requestor.species.return_value = [Specie(name="Human")]
    requestor.vehicles.return_value = [Vehicle(name="Tribubble bongo")]
    requestor.pilots.return_value = [
        Pilot(
            name="Anakin Skywalker",
            height="88",
            mass="84",
            gender="male",
            birth_year="41.9BBY",
            species=[1],
            vehicles=[44, 46],
            planet=1,
        )
    ]
    requestor.starships.return_value = [
        StarShip(
            name="Naboo star skiff",
            model="J-type star skiff",
            cost="unknown",
            velocity="1050",
            load_capacity="unknown",
            passengers="3",
            pilots=[]
        )
    ]

    handler = MigrationHandler(requestor, storage)
    response = handler.start()

    assert response.get("message") == "migration complete"

    storage.vehicles.assert_called_once()
    storage.species.assert_called_once()
    storage.planets.assert_called_once()
    storage.pilots.assert_called_once()
    storage.starships.assert_called_once()

    requestor.planets.assert_called_once()
    requestor.species.assert_called_once()
    requestor.vehicles.assert_called_once()
    requestor.pilots.assert_called_once()
    requestor.starships.assert_called_once()