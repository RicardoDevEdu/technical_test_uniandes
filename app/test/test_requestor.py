from typing import List

import pytest
import requests

from app.models.starship import StarShip
from app.services.requestor import Requestor, TOTAL_PAGE

TOTAL_RESULTS = 4

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
            "pilots": [],
            "starship_class": "corvette",
            "url": "https://swapi.py4e.com/api/starships/2/"
        }
    ]

def test_requestor_get(monkeypatch, mock_results_response):
    expected_results = StarShip(
        name="CR90 corvette",
        model="CR90 corvette",
        cost="3500000",
        velocity="950",
        load_capacity="3000000",
        passengers="600"
    )

    mock = MockResponse(mock_results_response)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock)

    requestor = Requestor()
    response = requestor.get()

    assert len(response) == TOTAL_RESULTS
    assert response[0] == expected_results


def test_error_requestor_get(monkeypatch, mock_results_response):
    mock = MockResponse(mock_results_response, is_error=True)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock)

    requestor = Requestor()

    with pytest.raises(requests.HTTPError) as err_info:
        requestor.get()

    assert str(err_info.value) == "Http error"