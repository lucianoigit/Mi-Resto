from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from enum import Enum as PyEnum
from enum import unique


@unique
class Turno(str, PyEnum):
    mañana = "mañana"
    tarde = "tarde"


class Cronograma(Base):
    __tablename__ = "Cronograma"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    turno = Column(Enum(Turno), nullable=False)
    empleado_id = Column(Integer, ForeignKey("Empleados.id"), nullable=False)

    empleado = relationship("Empleado", back_populates="cronograma")

    def __repr__(self):
        return f"<Cronograma(id={self.id}, fecha={self.fecha}, turno={self.turno}, empleado_id={self.empleado_id})>"