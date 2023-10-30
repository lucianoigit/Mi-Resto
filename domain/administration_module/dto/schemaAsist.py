from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class SchemaAttendanceBase(BaseModel):
    fecha: datetime
    presente: bool
    empleado_id: int


class SchemaAttendanceCreate(SchemaAttendanceBase):
    pass


class SchemaAttendance(SchemaAttendanceBase):
    id: int

    class Config:
        orm_mode = True
