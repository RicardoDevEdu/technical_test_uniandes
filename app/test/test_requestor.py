from typing import List

import pytest
import requests

from app.models.pilot import Pilot
from app.models.planet import Planet
from app.models.specie import Specie
from app.models.starship import StarShip
from app.models.vehicle import Vehicle
from app.services.requestor import Requestor, TOTAL_PAGE

TOTAL_RESULTS = 4
ITEMS_PER_PAGE = 10

class MockResponse:
    def __init__(self, results: List[dict], is_error: bool = False):
        self.results = results
        self.is_error = is_error

    def raise_for_status(self):
        if self.is_error:
            raise requests.HTTPError("Http error")

    def json(self):
        return {
            "count": 37,
            "next": "https://swapi.py4e.com/api/films/1/",
            "previous": None,
            "results": self.results
        }

@pytest.fixture
def mock_results_response():
    return [
        {
            "MGLT": "60",
            "cargo_capacity": "3000000",
            "consumables": "1 year",
            "cost_in_credits": "3500000",
            "created": "2014-12-10T14:20:33.369000Z",
            "crew": "30-165",
            "edited": "2014-12-20T21:23:49.867000Z",
            "films": ["https://swapi.py4e.com/api/films/1/", "https://swapi.py4e.com/api/films/3/", "https://swapi.py4e.com/api/films/6/"],
            "hyperdrive_rating": "2.0",
            "length": "150",
            "manufacturer": "Corellian Engineering Corporation",
            "max_atmosphering_speed": "950",
            "model": "CR90 corvette",
            "name": "CR90 corvette",
            "passengers": "600",
            "pilots": [
                "https://swapi.py4e.com/api/people/10/",
                "https://swapi.py4e.com/api/people/35/"
            ],
            "starship_class": "corvette",
            "url": "https://swapi.py4e.com/api/starships/2/"
        }
    ]

@pytest.fixture
def mock_results_response_pilots():
    return [
        {
            "name": "Biggs Darklighter",
            "height": "183",
            "mass": "84",
            "hair_color": "black",
            "skin_color": "light",
            "eye_color": "brown",
            "birth_year": "24BBY",
            "gender": "male",
            "homeworld": "https://swapi.py4e.com/api/planets/1/",
            "films": [
                "https://swapi.py4e.com/api/films/1/"
            ],
            "species": [
                "https://swapi.py4e.com/api/species/1/"
            ],
            "vehicles": [
                "https://swapi.py4e.com/api/vehicles/30/"
            ],
            "starships": [
                "https://swapi.py4e.com/api/starships/12/"
            ],
            "created": "2014-12-10T15:59:50.509000Z",
            "edited": "2014-12-20T21:17:50.323000Z",
            "url": "https://swapi.py4e.com/api/people/9/"
        }
    ]

@pytest.fixture
def mock_results_response_vehicles():
    return [
        {
            "name": "Sand Crawler",
            "model": "Digger Crawler",
            "manufacturer": "Corellia Mining Corporation",
            "cost_in_credits": "150000",
            "length": "36.8 ",
            "max_atmosphering_speed": "30",
            "crew": "46",
            "passengers": "30",
            "cargo_capacity": "50000",
            "consumables": "2 months",
            "vehicle_class": "wheeled",
            "pilots": [],
            "films": [
                "https://swapi.py4e.com/api/films/1/",
                "https://swapi.py4e.com/api/films/5/"
            ],
            "created": "2014-12-10T15:36:25.724000Z",
            "edited": "2014-12-20T21:30:21.661000Z",
            "url": "https://swapi.py4e.com/api/vehicles/4/"
        }
    ]

@pytest.fixture
def mock_results_response_species():
    return [
        {
            "name": "Droid",
            "classification": "artificial",
            "designation": "sentient",
            "average_height": "n/a",
            "skin_colors": "n/a",
            "hair_colors": "n/a",
            "eye_colors": "n/a",
            "average_lifespan": "indefinite",
            "homeworld": None,
            "language": "n/a",
            "people": [
                "https://swapi.py4e.com/api/people/2/",
                "https://swapi.py4e.com/api/people/3/",
                "https://swapi.py4e.com/api/people/8/",
                "https://swapi.py4e.com/api/people/23/",
                "https://swapi.py4e.com/api/people/87/"
            ],
            "films": [
                "https://swapi.py4e.com/api/films/1/",
                "https://swapi.py4e.com/api/films/2/",
                "https://swapi.py4e.com/api/films/3/",
                "https://swapi.py4e.com/api/films/4/",
                "https://swapi.py4e.com/api/films/5/",
                "https://swapi.py4e.com/api/films/6/",
                "https://swapi.py4e.com/api/films/7/"
            ],
            "created": "2014-12-10T15:16:16.259000Z",
            "edited": "2014-12-20T21:36:42.139000Z",
            "url": "https://swapi.py4e.com/api/species/2/"
        },

    ]

@pytest.fixture
def mock_results_response_planet():
    return [
        {
            "name": "Tatooine",
            "rotation_period": "23",
            "orbital_period": "304",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "surface_water": "1",
            "population": "200000",
            "residents": [
                "https://swapi.py4e.com/api/people/1/",
                "https://swapi.py4e.com/api/people/2/",
            ],
            "films": [
                "https://swapi.py4e.com/api/films/1/",
                "https://swapi.py4e.com/api/films/3/",
                "https://swapi.py4e.com/api/films/4/",
                "https://swapi.py4e.com/api/films/5/",
                "https://swapi.py4e.com/api/films/6/"
            ],
            "created": "2014-12-09T13:50:49.641000Z",
            "edited": "2014-12-20T20:58:18.411000Z",
            "url": "https://swapi.py4e.com/api/planets/1/"
        },
    ]


def test_requestor_get(monkeypatch, mock_results_response):
    expected_results = StarShip(
        name="CR90 corvette",
        model="CR90 corvette",
        cost="3500000",
        velocity="950",
        load_capacity="3000000",
        passengers="600",
        pilots=[10, 35]
    )

    mock = MockResponse(mock_results_response)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock)

    requestor = Requestor()
    response = requestor.starships()

    assert len(response) == TOTAL_RESULTS
    assert response[0] == expected_results

def test_error_requestor_get(monkeypatch, mock_results_response):
    mock = MockResponse(mock_results_response, is_error=True)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock)

    requestor = Requestor()

    with pytest.raises(requests.HTTPError) as err_info:
        requestor.starships()

    assert str(err_info.value) == "Http error"

def test_requestor_get_pilots(monkeypatch, mock_results_response_pilots):
    total_results = round(87/ITEMS_PER_PAGE)
    expected_results = Pilot(
        name="Biggs Darklighter",
        height="183",
        mass="84",
        gender="male",
        birth_year="24BBY",
        homeworld=1,
        species=[1],
        vehicles=[30],
        id=9
    )

    mock = MockResponse(mock_results_response_pilots)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock)

    requestor = Requestor()
    response = requestor.pilots()

    assert len(response) == total_results
    assert response[0] == expected_results

def test_requestor_get_vehicles(monkeypatch, mock_results_response_vehicles):
    total_results = round(39/ITEMS_PER_PAGE)
    expected_results = Vehicle(
        name="Sand Crawler",
        id=4
    )

    mock = MockResponse(mock_results_response_vehicles)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock)

    requestor = Requestor()
    response = requestor.vehicles()

    assert len(response) == total_results
    assert response[0] == expected_results

def test_requestor_get_species(monkeypatch, mock_results_response_species):
    total_results = round(37/ITEMS_PER_PAGE)
    expected_results = Specie(
        name="Droid",
        id=2
    )

    mock = MockResponse(mock_results_response_species)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock)

    requestor = Requestor()
    response = requestor.species()

    assert len(response) == total_results
    assert response[0] == expected_results

def test_requestor_get_planet(monkeypatch, mock_results_response_planet):
    total_results = round(61/ITEMS_PER_PAGE)
    expected_results = Planet(
        name="Tatooine",
        id=1
    )

    mock = MockResponse(mock_results_response_planet)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock)

    requestor = Requestor()
    response = requestor.planets()

    assert len(response) == total_results
    assert response[0] == expected_results