from typing import List
from unittest.mock import MagicMock

import pytest
from sqlmodel import Session

from app.models.database import StarshipModel, VehicleModel, SpecieModel, PlanetModel, PilotModel, PilotSpecieModel, \
    PilotVehicleModel
from app.models.domain import StarShip, Vehicle, Specie, Planet, Pilot, PilotResult
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

def test_storage_get_all_starships(monkeypatch, get_session):
    service = storage.Storage(get_session)

    get_session.exec.return_value.all.return_value = [
        StarshipModel(
            id=1,
            name="interceptor",
            model="Eta-2 Actis-class light interceptor",
            cost="320000",
            velocity="1500",
            load_capacity="60",
            passengers="0"
        )
    ]
    get_session.commit.return_value = None
    get_session.refresh.return_value = None

    results = service.get_all_starships()

    assert len(results) == 1
    assert results[0].id == 1
    assert results[0].name == "interceptor"
    assert results[0].model == "Eta-2 Actis-class light interceptor"
    assert results[0].cost == "320000"
    assert results[0].velocity == "1500"
    assert results[0].load_capacity == "60"
    assert results[0].passengers == "0"

    get_session.exec.return_value.all.assert_called_once()

def test_storage_get_starship(monkeypatch, get_session):
    service = storage.Storage(get_session)

    get_session.exec.return_value.first.return_value = StarshipModel(
            id=1,
            name="interceptor",
            model="Eta-2 Actis-class light interceptor",
            cost="320000",
            velocity="1500",
            load_capacity="60",
            passengers="0"
    )

    get_session.commit.return_value = None
    get_session.refresh.return_value = None

    results = service.get_starship(1)

    assert results.id == 1
    assert results.name == "interceptor"
    assert results.model == "Eta-2 Actis-class light interceptor"
    assert results.cost == "320000"
    assert results.velocity == "1500"
    assert results.load_capacity == "60"
    assert results.passengers == "0"

    get_session.exec.return_value.first.assert_called_once()

def test_storage_update_starship(monkeypatch, get_session, get_session_mock_return):
    service = storage.Storage(get_session)

    get_session.exec.return_value.first.return_value = StarshipModel(
            id=1,
            name="interceptor",
            model="Eta-2 Actis-class light interceptor",
            cost="320000",
            velocity="1500",
            load_capacity="60",
            passengers="0"
    )

    get_session.add.return_value = None
    get_session.commit.return_value = None
    get_session.refresh.return_value = None

    starship = StarShip(
        id=1,
        name="interceptor new",
        model="Eta-2 Actis-class light interceptor change",
        cost="320000",
        velocity="1500",
        load_capacity="60",
        passengers="0"
    )

    results = service.update_starship(1, starship)

    expected_params: StarshipModel = StarshipModel(
            id=1,
            name="interceptor new",
            model="Eta-2 Actis-class light interceptor change",
            cost="320000",
            velocity="1500",
            load_capacity="60",
            passengers="0"
    )

    assert results.name == "interceptor new"
    assert results.model == "Eta-2 Actis-class light interceptor change"

    get_session.add.assert_called_with(expected_params)
    get_session.exec.return_value.first.assert_called_once()
    get_session.add.assert_called_once()

def test_storage_get_all_pilots(monkeypatch, get_session):
    service = storage.Storage(get_session)

    pilot = MagicMock(spec=PilotModel)
    pilot.id = 1
    pilot.name = "Anakin Skywalker"
    pilot.height = "00"
    pilot.mass = "00"
    pilot.gender = "male",
    pilot.birth_year = "41.9BBY",

    get_session.exec.return_value.unique.return_value = [
        pilot
    ]

    results = service.get_all_pilots()

    assert len(results) == 1
    assert results[0].id == 1
    assert results[0].name == "Anakin Skywalker"
    assert results[0].height == "00"
    assert results[0].mass == "00"
    assert results[0].gender == ('male',)
    assert results[0].birth_year == ('41.9BBY',)

    get_session.exec.return_value.unique.assert_called_once()