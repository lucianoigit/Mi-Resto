from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base



class Mesa(Base):
    __tablename__ = "Mesas"
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=False)
   