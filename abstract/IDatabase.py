from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from db.database import Base
from sqlalchemy.orm import Session

T = TypeVar("T", bound=Base)


class IDatabase(Generic[T]):
    @abstractmethod
    def get_database(self, db_Session: Session) -> T | None:
        pass 


