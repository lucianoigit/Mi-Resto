from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Rol(Base):
    __tablename__ = "Roles"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)


    def __repr__(self):
        return f"<Rol(id={self.id}, nombre=\"{self.nombre}\")>" 


    empleados = relationship("Empleado", back_populates="rol") 