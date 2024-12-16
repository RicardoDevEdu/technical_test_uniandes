from typing import Protocol, List

from app.models.domain import Pilot, PilotResult


class PilotStorer(Protocol):
    def get_all_pilots(self) -> List[PilotResult]: ...


class PilotHandler:
    def __init__(self, storage: PilotStorer):
        self.storage = storage

    def get_all_pilots(self) -> List[PilotResult]:
        return self.storage.get_all_pilots()