from typing import List

from app.dependencies.database import SessionDep
from app.models.database import VehicleModel, SpecieModel, PlanetModel, PilotSpecieModel, PilotModel, PilotVehicleModel, \
    StarshipModel
from app.models.domain import Pilot, Planet, Specie, Vehicle, StarShip


class Storage:
    def __init__(self, session_db: SessionDep):
        self.session_db = session_db

    def starships(self, starships: List[StarShip]) -> None:
        starship_model: List[VehicleModel] = []

        for starship in starships:
            starship_model.append(StarshipModel(
                name=starship.name,
                model=starship.model,
                cost=starship.cost,
                velocity=starship.velocity,
                load_capacity=starship.load_capacity,
                passengers=starship.passengers,
            ))
        self.session_db.add_all(starship_model)
        self.session_db.commit()


    def vehicles(self, vehicles: List[Vehicle]) -> None:
        vehicles_model: List[VehicleModel] = []
        for vehicle in vehicles:
            vehicles_model.append(VehicleModel(**vehicle.__dict__))

        self.session_db.add_all(vehicles_model)
        self.session_db.commit()


    def pilots(self, pilots: List[Pilot]) -> None:
        for pilot in pilots:
            pilots_model: PilotModel = PilotModel(
                name=pilot.name,
                height=pilot.height,
                mass=pilot.mass,
                gender=pilot.gender,
                birth_year=pilot.birth_year,
                planet_id=pilot.planet,
            )
            self.session_db.add(pilots_model)
            self.session_db.commit()
            self.session_db.refresh(pilots_model)

            if len(pilot.species) > 0:
                pilot_specie_model: PilotSpecieModel = PilotSpecieModel(
                    specie_id=pilot.species[0],
                    pilot_id=pilots_model.id,
                )
                self.session_db.add(pilot_specie_model)
                self.session_db.commit()
                self.session_db.refresh(pilot_specie_model)

            if len(pilot.vehicles) > 0:
                for vehicle in pilot.vehicles:
                    pilot_vehicle_model: PilotVehicleModel = PilotVehicleModel(
                        vehicle_id=vehicle,
                        pilot_id=pilots_model.id,
                    )
                    self.session_db.add(pilot_vehicle_model)
                    self.session_db.commit()
                    self.session_db.refresh(pilot_vehicle_model)


    def species(self, species: List[Specie]) -> None:
        species_model: List[SpecieModel] = []
        for specie in species:
            species_model.append(SpecieModel(**specie.__dict__))

        self.session_db.add_all(species_model)
        self.session_db.commit()
        self.session_db.refresh(species_model)


    def planets(self, planets: List[Planet]) -> None:
        planets_model: List[PlanetModel] = []
        for planet in planets:
            planets_model.append(PlanetModel(**planet.__dict__))

        self.session_db.add_all(planets_model)
        self.session_db.commit()
