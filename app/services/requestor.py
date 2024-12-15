import re
from typing import List

import requests

from app.models.domain import Pilot, Planet, Specie, StarShip, Vehicle

BASE_URL = "https://swapi.py4e.com/api/"
TOTAL_PAGE = 4
ITEMS_PER_PAGE = 10

class Requestor:
     def starships(self) -> List[StarShip]:
         start_ships: List[StarShip] = []

         for page in range(TOTAL_PAGE):
             url: str = f"{BASE_URL}starships/?page={page+1}"

             response = requests.get(url)
             response.raise_for_status()
             data = response.json()

             results = data["results"]

             for starship in results:
                 start_ships.append(
                     StarShip(
                         name=starship["name"],
                         model=starship["model"],
                         cost=starship["cost_in_credits"],
                         velocity=starship["max_atmosphering_speed"],
                         load_capacity=starship["cargo_capacity"],
                         passengers=starship["passengers"],
                         pilots=self._extract_id_to_list(starship["pilots"]),
                     )
                 )

         return start_ships

     def pilots(self) -> List[Pilot]:
         pilots: List[Pilot] = []
         items: int = 87
         total_results = round(items / ITEMS_PER_PAGE)

         for page in range(total_results):
             url: str = f"{BASE_URL}people/?page={page+1}"

             response = requests.get(url)
             response.raise_for_status()
             data = response.json()

             results = data["results"]

             for pilot in results:
                 pilots.append(
                     Pilot(
                         id=self._extract_id(pilot["url"]),
                         name=pilot["name"],
                         height=pilot["height"],
                         mass=pilot["mass"],
                         gender=pilot["gender"],
                         birth_year=pilot["birth_year"],
                         planet=self._extract_id(pilot["homeworld"]),
                         species=self._extract_id_to_list(pilot["species"]),
                         vehicles=self._extract_id_to_list(pilot["vehicles"]),
                     )
                 )
         return pilots

     def vehicles(self) -> List[Vehicle]:
         vehicles: List[Vehicle] = []
         items: int = 39
         total_results = round(items / ITEMS_PER_PAGE)

         for page in range(total_results):
             url: str = f"{BASE_URL}vehicles/?page={page + 1}"

             response = requests.get(url)
             response.raise_for_status()
             data = response.json()

             results = data["results"]

             for vehicle in results:
                 vehicles.append(
                     Vehicle(
                         id=self._extract_id(vehicle["url"]),
                         name=vehicle["name"]
                     )
                 )
         return vehicles

     def species(self) -> List[Specie]:
         species: List[Specie] = []
         items: int = 37
         total_results = round(items / ITEMS_PER_PAGE)

         for page in range(total_results):
             url: str = f"{BASE_URL}species/?page={page + 1}"

             response = requests.get(url)
             response.raise_for_status()
             data = response.json()

             results = data["results"]

             for specie in results:
                 species.append(
                     Specie(
                         id=self._extract_id(specie["url"]),
                         name=specie["name"]
                     )
                 )
         return species

     def planets(self) -> List[Planet]:
         planets: List[Planet] = []
         items: int = 61
         total_results = round(items / ITEMS_PER_PAGE)

         for page in range(total_results):
             url: str = f"{BASE_URL}planets/?page={page + 1}"

             response = requests.get(url)
             response.raise_for_status()
             data = response.json()

             results = data["results"]

             for planet in results:
                 planets.append(
                     Planet(
                         id=self._extract_id(planet["url"]),
                         name=planet["name"]
                     )
                 )
         return planets

     def _extract_id(self, url: str) -> int:
         match = re.search(r'/(\d+)/$', url)
         if match:
             return int(match.group(1))
         raise ValueError("id not found")

     def _extract_id_to_list(self, urls: List[str])-> List[int]:
         ids: List[int] = []
         for url in urls:
             ids.append(self._extract_id(url))
         return ids
