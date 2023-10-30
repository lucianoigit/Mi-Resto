from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from administration_module.dto.schemaEmployee import SchemaEmployeeBase


class SchemaAdministrativoBase(SchemaEmployeeBase):
    pass


class SchemaAdministrativoCreate(SchemaAdministrativoBase):
    pass


class SchemaAdministrativo(SchemaAdministrativoBase):
    id: int

    class Config:
        orm_mode = True
