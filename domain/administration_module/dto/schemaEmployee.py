from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class SchemaEmployeeBase(BaseModel):
    nombre: str
    apellido: str
    edad: int
    email: Optional[str] = None
    rol_id: Optional[int]  # Usa SchemaRolBase en lugar de SchemaRol """


class SchemaEmployeeCreate(SchemaEmployeeBase):
    pass


class SchemaEmployee(SchemaEmployeeBase):
    id: int

    class Config:
        orm_mode = True


class EmployeeResponse(BaseModel):
    empleado: SchemaEmployee
