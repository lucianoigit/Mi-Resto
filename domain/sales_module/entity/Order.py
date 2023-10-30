import datetime
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class Order(Base):
    __tablename__ = "Orders"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255))
    create_at = Column(DateTime, default=datetime.utcnow)
    is_payd = Column(Boolean, default=False)
    is_delivered = Column(Boolean, default=False)
    empleado_id = Column(Integer, ForeignKey(
        "Empleados.id"), nullable=True, default=1)
    mesa_id = Column(Integer, ForeignKey("Mesas.id"), nullable=False)

    empleado = relationship("Empleado", back_populates="orders")
