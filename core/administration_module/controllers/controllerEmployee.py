from fastapi import HTTPException, Depends
import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from core.administration_module.services.admin import AdminService
from container.container import Container
from dependency_injector.wiring import Provide, inject
from domain.administration_module.dto.schemaAsingRole import SchemaAsingRoleBase
from domain.administration_module.dto.schemaEmployee import EmployeeResponse, SchemaEmployee, SchemaEmployeeCreate
router = APIRouter(
    prefix='/empleados',
    tags=['empleados'],
)

logging.warning("accediendo al crud")


@router.post("")
@inject
def create_employee(
    empleado_data: SchemaEmployeeCreate,
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider]),
):
    new_empleado = admin_service_class.create_empleado(empleado_data)
    return new_empleado


@router.get("/{empleado_id}", response_model=SchemaEmployeeCreate)
@inject
def get_employee_by_id(
    empleado_id: int,
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider]),
) -> EmployeeResponse:
    empleado = admin_service_class.get_empleado_by_id(empleado_id)
    return empleado


@router.get("/", response_model=List[SchemaEmployee])
@inject
def get_all_employees(
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider])
) -> List[SchemaEmployee]:
    empleados = admin_service_class.get_all_empleados()
    return empleados


@router.delete("/{empleado_id}", response_model=SchemaEmployee)
@inject
def delete_employee(
    empleado_id: int,
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider])
):
    deleted_empleado = admin_service_class.delete_empleado(empleado_id)
    if deleted_empleado:
        return f"Se eliminó el item {empleado_id}"


@router.put("/asing-role")
@inject
def asing_role(
    asing_data: SchemaAsingRoleBase,
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider]),
):
    result = admin_service_class.asing_rol(
        asing_data.empleado_id, asing_data.rol_id)

    if result is not None:
        return result  # Devuelve la respuesta de la función, que podría incluir un mensaje de éxito y detalles del empleado asignado
    else:
        # Maneja el caso en que la función devuelve None
        raise HTTPException(
            status_code=404, detail="Error al asignar rol. Verifica los parámetros y el estado de la base de datos.")
