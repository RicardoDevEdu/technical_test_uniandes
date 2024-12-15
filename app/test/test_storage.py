from typing import List
from unittest.mock import MagicMock

import pytest
from sqlmodel import Session

from app.models.database import StarshipModel, VehicleModel, SpecieModel, PlanetModel, PilotModel, PilotSpecieModel, \
    PilotVehicleModel
from app.models.domain import StarShip, Vehicle, Specie, Planet, Pilot
from app.services import storage


@pytest.fixture
def get_session() -> MagicMock:
    return MagicMock(autospec=Session)

@pytest.fixture
def get_session_mock_return(get_session):
    get_session.add_all.return_value = None
    get_session.commit.return_value = None
    get_session.refresh.return_value = None


def test_storage_starships(monkeypatch, get_session, get_session_mock_return):
    service = storage.Storage(get_session)
    starships: List[StarShip] = [
        StarShip(
            name="Naboo star skiff",
            model="J-type star skiff" ,
            cost="unknown",
            velocity="1050",
            load_capacity="unknown",
            passengers="3",
            pilots=[]
        ),
        StarShip(
            name="Jedi Interceptor",
            model="Eta-2 Actis-class light interceptor" ,
            cost="320000",
            velocity="1500",
            load_capacity="60",
            passengers="0",
            pilots=[]
        ),
    ]

    service.starships(starships=starships)

    expected_params: List[StarshipModel] = [
        StarshipModel(
            name="Naboo star skiff",
            model="J-type star skiff",
            cost="unknown",
            velocity="1050",
            load_capacity="unknown",
            passengers="3",
        ),
        StarshipModel(
            name="Jedi Interceptor",
            model="Eta-2 Actis-class light interceptor",
            cost="320000",
            velocity="1500",
            load_capacity="60",
            passengers="0",
        ),
    ]

    get_session.add_all.assert_called_with(expected_params)
    get_session.add_all.assert_called_once()
    get_session.commit.assert_called_once()

def test_storage_vehicles(monkeypatch, get_session, get_session_mock_return):
    service = storage.Storage(get_session)
    vehicles: List[Vehicle] = [
        Vehicle(name="Tribubble bongo")
    ]

    service.vehicles(vehicles)

    expected_params: List[VehicleModel] = [
        VehicleModel(
            name="Tribubble bongo",
        )
    ]

    get_session.add_all.assert_called_with(expected_params)
    get_session.add_all.assert_called_once()
    get_session.commit.assert_called_once()

def test_storage_pilots(monkeypatch, get_session, get_session_mock_return):
    service = storage.Storage(get_session)
    pilots: List[Pilot] = [
        Pilot(
            name= "Anakin Skywalker",
            height= "88",
            mass= "84",
            gender= "male",
            birth_year= "41.9BBY",
            species= [1],
            vehicles= [44, 46],
            planet= 1,
            id= 1
        )
    ]

    service.pilots(pilots)
    expected_params: PilotModel = PilotModel(
            name= "Anakin Skywalker",
            height= "88",
            mass= "84",
            gender= "male",
            birth_year= "41.9BBY",
            planet_id=1
        )

    pilot_species = PilotSpecieModel(specie_id=1, pilot_id=None, id=None)
    pilot_vehicles: List[PilotVehicleModel] = [
        PilotVehicleModel(vehicle_id=44, pilot_id=None, id=None),
        PilotVehicleModel(vehicle_id=46, pilot_id=None, id=None)
    ]

    assert get_session.add.call_count == 4


    expected_calls = [
        (expected_params,),
        (pilot_species,),
        (pilot_vehicles[0],),
        (pilot_vehicles[1],)
    ]

    actual_calls = [call.args for call in get_session.add.call_args_list]

    assert actual_calls == expected_calls


def test_storage_species(monkeypatch, get_session, get_session_mock_return):
    service = storage.Storage(get_session)
    species: List[Specie] = [
        Specie(name="Human")
    ]

    service.species(species)

    expected_params: List[SpecieModel] = [
        SpecieModel(
            name="Human",
        )
    ]

    get_session.add_all.assert_called_with(expected_params)
    get_session.add_all.assert_called_once()
    get_session.commit.assert_called_once()

def test_storage_planets(monkeypatch, get_session, get_session_mock_return):
    service = storage.Storage(get_session)
    planets: List[Planet] = [
        Planet(name="Tatooine")
    ]

    service.planets(planets)

    expected_params: List[PlanetModel] = [
        PlanetModel(
            name="Tatooine",
        )
    ]

    get_session.add_all.assert_called_with(expected_params)
    get_session.add_all.assert_called_once()
    get_session.commit.assert_called_once()