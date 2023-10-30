from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional



class SchemaRolBase(BaseModel):
    nombre: str

class SchemaRolCreate(SchemaRolBase):
    pass

class SchemaRol(SchemaRolBase):
    id: int

    class Config:
        orm_mode = True

class RolResponse(BaseModel):
    rol: SchemaRol

class RolAllResponse(BaseModel):
    roles: List[SchemaRol]
    