from typing import List

from fastapi import APIRouter, Depends

from app.handlers.StarshipHandler import StarshipHandler
from app.models.domain import StarShip
from app.services.storage import Storage

router = APIRouter()

@router.get("/starships", response_model=List[StarShip])
def get_starships(store = Depends(Storage)):
    handler = StarshipHandler(store)
    return handler.get_all()


@router.get("/starships/{id}", response_model=StarShip)
def get_starships(id: int, store = Depends(Storage)):
    handler = StarshipHandler(store)
    return handler.get_starship(id=id)


@router.put(
    "/starships/{id}",
    response_model=StarShip,
)
def put_starship(id: int, starship: StarShip, store = Depends(Storage)):
    handler = StarshipHandler(store)
    return handler.update_starship(id=id, starship=starship)
