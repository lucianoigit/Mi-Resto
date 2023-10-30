from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy import Column, Integer
from db.database import Base
from sqlalchemy.orm import Session

T = TypeVar("T", bound=Base)


class IEntity(ABC):
    id = Column(Integer, primary_key=True, index=True)
