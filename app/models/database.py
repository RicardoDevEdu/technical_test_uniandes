from sqlmodel import SQLModel, Field, Relationship


class PilotSpecieModel(SQLModel, table=True):
    __tablename__ = 'pilot_species'

    id: int =  Field(default=None, primary_key=True)
    specie_id: int = Field(foreign_key="species.id")
    pilot_id: int = Field(foreign_key="pilots.id")


class PilotVehicleModel(SQLModel, table=True):
    __tablename__ = 'pilot_vehicles'

    id: int = Field(foreign_key="species.id")
    vehicle_id: int = Field(foreign_key="vehicles.id")
    pilot_id: int = Field(foreign_key="pilots.id")


class PilotModel(SQLModel, table=True):
    __tablename__ = 'pilots'

    id:int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    height: str = Field(default=None)
    mass: str = Field(default=None)
    gender: str = Field(default=None)
    birth_year: str = Field(default=None)
    species: list["SpecieModel"] = Relationship(
        back_populates="pilots", link_model=PilotSpecieModel
    )


class SpecieModel(SQLModel, table=True):
    __tablename__ = 'species'

    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    pilots: list[PilotModel] = Relationship(
        back_populates='species', link_model=PilotSpecieModel
    )


class VehicleModel(SQLModel, table=True):
    __tablename__ = 'vehicles'

    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)


class PlanetModel(SQLModel, table=True):
    __tablename__ = 'planets'

    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)


class StarshipModel(SQLModel, table=True):
    __tablename__ = 'starships'

    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    model: str = Field(default=None)
    cost: str = Field(default=None)
    velocity: str = Field(default=None)
    load_capacity: str = Field(default=None)
    passengers: str = Field(default=None)
