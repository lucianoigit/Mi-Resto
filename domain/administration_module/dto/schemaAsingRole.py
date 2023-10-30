from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional



class SchemaAsingRoleBase(BaseModel):
    empleado_id: int
    rol_id: int  