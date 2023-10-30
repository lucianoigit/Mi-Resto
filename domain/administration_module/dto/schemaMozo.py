from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from administration_module.dto.schemaEmployee import SchemaEmployeeBase
from schemaAsist import SchemaAttendance


class SchemaMozoBase(SchemaEmployeeBase):
    pass


class SchemaMozoCreate(SchemaMozoBase):
    pass


class SchemaMozo(SchemaMozoBase):
    id: int
    asistencias: List['SchemaAttendance'] = []

    class Config:
        orm_mode = True
