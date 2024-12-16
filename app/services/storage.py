from typing import List

from sqlalchemy.orm import joinedload
from sqlmodel import select

from app.dependencies.database import SessionDep
from app.models.database import VehicleModel, SpecieModel, PlanetModel, PilotSpecieModel, PilotModel, PilotVehicleModel, \
    StarshipModel
from app.models.domain import Pilot, Planet, Specie, Vehicle, StarShip, PilotResult


class Storage:
    def __init__(self, session_db: SessionDep):
        self.session_db = session_db

    def starships(self, starships: List[StarShip]) -> None:
        starship_model: List[StarshipModel] = []

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


    def planets(self, planets: List[Planet]) -> None:
        planets_model: List[PlanetModel] = []
        for planet in planets:
            planets_model.append(PlanetModel(**planet.__dict__))

        self.session_db.add_all(planets_model)
        self.session_db.commit()


    def get_all_starships(self) -> List[StarShip]:
        starships: List[StarShip] = []
        query = (
            select(StarshipModel)
        )

        result = self.session_db.exec(query).all()
        for starship in result:
            starships.append(
                StarShip(
                    id=starship.id,
                    name=starship.name,
                    model=starship.model,
                    cost=starship.cost,
                    velocity=starship.velocity,
                    load_capacity=starship.load_capacity,
                    passengers=starship.passengers,
                    pilots=[]
                )
            )

        return starships


    def get_starship(self, id: int) -> StarShip:
        query = (
            select(StarshipModel).
            where(StarshipModel.id == id)
        )

        result = self.session_db.exec(query).first()
        return StarShip(
            id=result.id,
            name=result.name,
            model=result.model,
            cost=result.cost,
            velocity=result.velocity,
            load_capacity=result.load_capacity,
            passengers=result.passengers,
            pilots=[]
        )
    
    
    def update_starship(self, id: int, starship: StarShip) -> StarShip:
        query = (
            select(StarshipModel).
            where(StarshipModel.id == id)
        )

        result = self.session_db.exec(query).first()
        if result is None:
            raise Exception(f"Starship with id:{id} not found")

        result.name = starship.name
        result.model = starship.model
        result.cost = starship.cost
        result.velocity = starship.velocity
        result.load_capacity = starship.load_capacity
        result.passengers = starship.passengers

        self.session_db.add(result)
        self.session_db.commit()
        self.session_db.refresh(result)

        return StarShip(
            id=result.id,
            name=starship.name,
            model=starship.model,
            cost=starship.cost,
            velocity=starship.velocity,
            load_capacity=starship.load_capacity,
            passengers=starship.passengers,
        )


    def get_all_pilots(self) -> List[PilotResult]:
        pilots: List[PilotResult] = []
        query = (
            select(
                PilotModel
            )
            .options(
                joinedload(PilotModel.species),
                joinedload(PilotModel.vehicles),
                joinedload(PilotModel.planet)
            )
        )

        results = self.session_db.exec(query).unique()

        for  pilot in results:
            pilots.append(
                PilotResult(
                    id=pilot.id,
                    name=pilot.name,
                    height=pilot.height,
                    mass=pilot.mass,
                    gender=pilot.gender,
                    birth_year=pilot.birth_year,
                    species=pilot.species,
                    vehicles=pilot.vehicles,
                    planet=pilot.planet,
                )
            )

        return pilots

