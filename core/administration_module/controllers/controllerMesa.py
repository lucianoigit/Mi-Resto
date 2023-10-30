import logging
from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from domain.administration_module.dto.schemaMesa import *
from core.administration_module.services.admin import AdminService
from core.administration_module.services.mesa import MesaService
from container.container import Container
from dependency_injector.wiring import Provide, inject
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter(
    prefix='/mesas',
    tags=['mesas'],
)


@router.post("",)
@inject
def create_mesa(mesa_data: SchemaMesaCreate,
                mesa_service_class: MesaService = Depends(Provide[Container.service_mesa_provider])):
    new_mesa = mesa_service_class.create_mesa(mesa_data)
    return new_mesa
