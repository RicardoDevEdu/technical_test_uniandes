from typing import List

from fastapi import APIRouter, Depends

from app.handlers.PilotHandler import PilotHandler
from app.models.domain import Pilot, PilotResult
from app.services.storage import Storage

router = APIRouter()

@router.get("/pilots" , response_model=List[PilotResult])
def get_pilots(storage = Depends(Storage)) -> List[PilotResult]:
    handler = PilotHandler(storage)

    return handler.get_all_pilots()