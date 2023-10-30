import logging
from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from domain.administration_module.dto.schemaAsist import *
from core.administration_module.services.admin import AdminService
from container.container import Container
from dependency_injector.wiring import Provide, inject
from sqlalchemy.exc import SQLAlchemyError
from fastapi import status

router = APIRouter(
    prefix='/asistencias',
    tags=['asistencias'],
)


@router.post("")
@inject
def create_asistence(asistence_data: SchemaAttendanceCreate,
                     admin_service_class: AdminService = Depends(Provide[Container.service_admin_provider])):
    empleado_asist = admin_service_class.create_asistence(asistence_data)
    return empleado_asist


@router.get("")
@inject
def get_all_asistences(admin_service_class: AdminService = Depends(Provide[Container.service_admin_provider])
                       ) -> List[SchemaAttendance]:
    asistences = admin_service_class.get_all_empleados_asist()
    return asistences


@router.get("/{id}")
@inject
def get_asistence_by_id(id: int, admin_service_class: AdminService = Depends(Provide[Container.service_admin_provider])
                        ) -> SchemaAttendance:
    asistences = admin_service_class.get_asistence_by_id(id)
    return asistences
