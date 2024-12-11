from typing import List

import requests

from app.models.starship import StarShip

BASE_URL = "https://swapi.py4e.com/api/"
TOTAL_PAGE = 4

class Requestor:
     def get(self) -> List[StarShip]:
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
                     )
                 )

         return start_ships