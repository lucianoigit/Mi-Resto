from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base
from .Employee import Empleado


class Administrativo(Empleado):
    __tablename__ = "Administrativos"
    id = Column(Integer, ForeignKey("Empleados.id"), primary_key=True)

    # Puedes agregar relaciones o atributos específicos para administrativos si es necesario
