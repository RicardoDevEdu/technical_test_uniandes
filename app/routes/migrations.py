from fastapi import APIRouter, Depends
from sqlmodel import select

from app.dependencies.database import SessionDep
from app.models.database import StarshipModel, PilotModel, PilotSpecieModel, SpecieModel
from app.services.requestor import Requestor
from app.handlers.MigrationHandler import MigrationHandler
from app.services.storage import Storage

router = APIRouter()

@router.post("/api/migrations", response_model=dict)
async def init_migrations(request = Depends(Requestor), store = Depends(Storage)):
    migrations = MigrationHandler(request, store)
    result = migrations.start()

    return result
