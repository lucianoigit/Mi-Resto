from typing import List
from pydantic import BaseModel
from datetime import datetime


class SchemaOrderBase(BaseModel):
    id: int
    description: str
    mesa_id: int
    is_payd: bool
    is_delivered: bool
    create_at: datetime


class SchemaOrderByEmployeCreate(SchemaOrderBase):
    empleado_id: int


class SchemaOrderByMesaCreate(SchemaOrderBase):
    pass


class SchemaOrder(SchemaOrderByEmployeCreate):
    pass


class SchemaOrderResponse(SchemaOrderBase):
    id: int


class SchemaOrderWithEmpleadoResponse(SchemaOrderResponse):
    empleado: dict


class SchemaOrderWithMesaResponse(SchemaOrderResponse):
    mesa: dict
