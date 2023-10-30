import logging
from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from core.administration_module.services.admin import AdminService
from domain.sales_module.dto.schemaOrder import *
from domain.sales_module.entity.Order import Order
from core.sales_module.services.SaleService import SaleService
from container.container import Container
from dependency_injector.wiring import Provide, inject
from sqlalchemy.exc import SQLAlchemyError
from fastapi import status
router = APIRouter(
    prefix='/orders',
    tags=['orders'],

)


@router.post("/empleado")
@inject
def create_order(
    order_data: SchemaOrderByEmployeCreate,
    sale_service_class: SaleService = Depends(
        Provide[Container.service_Sale_provider]),
    admin_service_class: AdminService = Depends(
        Provide[Container.service_admin_provider])
):
    query_asistence = admin_service_class.get_asistence_by_id(
        order_data.empleado_id)
    new_order = sale_service_class.create_order_by_employe(
        order_data, query_asistence)
    return new_order


@router.post("/mesa")
@inject
def create_order(
    order_data: SchemaOrderByMesaCreate,
    sale_service_class: SaleService = Depends(
        Provide[Container.service_Sale_provider]),
):

    new_order = sale_service_class.create_order_by_mesa(order_data)
    return new_order


@router.put("")
@inject
def update_order(order_data: SchemaOrder,
                 sales_service_class: SaleService = Depends(Provide[Container.service_Sale_provider])):

    sales_service_class.update_order(order_data)
    return None


@router.delete("{order_id}")
@inject
def delete_order(order_id: int, sales_service_class: SaleService = Depends(Provide[Container.service_Sale_provider])):

    sales_service_class.delete_order(order_id)
    return None


@router.get("{order_id}")
@inject
def get_order_by_id(order_id: int, sales_service_class: SaleService = Depends(Provide[Container.service_Sale_provider])) -> SchemaOrder:

    order = sales_service_class.get_order_by_id(order_id)
    return order


@router.get("", response_model=List[SchemaOrder])
@inject
def get_all_orders(sales_service_class: SaleService = Depends(Provide[Container.service_Sale_provider])) -> List[SchemaOrder]:

    orders = sales_service_class.get_all_orders()
    return orders
