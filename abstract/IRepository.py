""" from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from db import database



Model = TypeVar("Model", bound=database.Base)

class GenericRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Model | None:
        pass 

    @abstractmethod
    def get_all(self, **filters) -> list[Model]:
        pass 

    @abstractmethod
    def create(self, record: Model) -> Model:
        pass 

    @abstractmethod
    def update(self, record: Model) -> Model:
        pass 

    @abstractmethod
    def delete(self, id: int) -> None:
        pass 
 """