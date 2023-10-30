import logging
from typing import List, Union
from domain.administration_module.dto.schemaAsingRole import SchemaAsingRoleBase
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from domain.administration_module.dto.schemaEmployee import *
from core.administration_module.services.admin import AdminService
from core.administration_module.services.asingEmploye import AsingEmployeService
from container.container import Container
from dependency_injector.wiring import Provide, inject
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter(
    prefix='/asing-employe',
    tags=['asing-employe'],
)

logging.warning("accediendo al crud")


@router.put("/")
@inject
def asing_employe(
    order_id: int,
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider]),
    asing_service_class: AsingEmployeService = Depends(
        Provide[Container.service_orderEmploye_provider])
):
    empleados_asist = admin_service_class.get_all_empleados_asist()
    asing_service_class.asing_employe(empleados_asist, order_id)
