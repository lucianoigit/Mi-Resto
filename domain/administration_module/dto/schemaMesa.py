from typing import Optional
from pydantic import BaseModel

class SchemaMesaCreate(BaseModel):
    number:int
    

class SchemaMesaUpdate(SchemaMesaCreate):
    empleado_id: Optional[int] = None

class SchemaMesa(SchemaMesaCreate):
    id: int

class MesaInDB(SchemaMesa):
    class Config:
        orm_mode = True
