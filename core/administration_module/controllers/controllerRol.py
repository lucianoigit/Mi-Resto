import logging
from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from core.administration_module.services.admin import AdminService
from domain.administration_module.dto.schemaRol import RolAllResponse, RolResponse, SchemaRol, SchemaRolCreate
from container.container import Container
from dependency_injector.wiring import Provide, inject
from fastapi import status

router = APIRouter(
    prefix='/roles',
    tags=['roles'],
)

logging.warning("accediendo al crud")


@router.post("")
@inject
def create_rol(
    rol_data: SchemaRolCreate,
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider]),
):
    new_rol = admin_service_class.create_rol(rol_data)
    return new_rol


@router.get("/{rol_id}", response_model=SchemaRol)
@inject
def get_rol_by_id(
    rol_id: int,
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider]),
) -> RolResponse:

    rol = admin_service_class.get_rol_by_id(rol_id)
    if rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol


@router.get("/", response_model=List[SchemaRol])
@inject
def get_all_roles(
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider])
) -> List[SchemaRol]:
    roles = admin_service_class.get_all_rols()
    return roles


@router.delete("/{rol_id}")
@inject
def delete_rol(
    rol_id: int,
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider])
):
    deleted_rol = admin_service_class.delete_rol(rol_id)
    if deleted_rol:
        return f"Se eliminó el item {rol_id}"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El rol con ID {rol_id} no se encontró")
