""" from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base
from .Empleado import Empleado

class Mozo(Empleado):
    __tablename__ = "Mozos"
    id = Column(Integer, ForeignKey("Empleados.id"), primary_key=True)
    
    # Definir la relación con asistencia solo para mozos """
"""  asistencias = relationship("Asistencia", back_populates="mozo") """
