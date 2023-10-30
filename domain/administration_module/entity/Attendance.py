import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base

class Attendance(Base):
    __tablename__ = "Asistencias"
    id = Column(Integer, primary_key = True, index = True)
    empleado_id = Column(Integer, ForeignKey("Empleados.id"), nullable=False,unique=True)
    presente = Column(Boolean, default = True)
    fecha = Column(DateTime, default = datetime.utcnow)

    # Definir la relación con la tabla de empleados
    empleado = relationship("Empleado", back_populates="asistencias")

    def __repr__(self):
        return f"<Asistencia(id={self.id}, fecha={self.fecha}, empleado_id={self.empleado_id})>"