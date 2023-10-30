from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class Empleado(Base):
    __tablename__ = "Empleados"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    email = Column(String(100), nullable=True)
    rol_id = Column(Integer, ForeignKey("Roles.id"), nullable=False)
   
    
    
    rol = relationship("Rol", back_populates="empleados")
    asistencias = relationship("Asistencia", back_populates="empleado")
    orders = relationship("Order", back_populates = "empleado")


    def __repr__(self):
        return f"<Empleado(id={self.id}, nombre=\"{self.nombre}\")>"
