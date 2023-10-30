import logging
import traceback
from typing import List, Optional
from fastapi import Depends
from domain.administration_module.dto.schemaAsist import SchemaAttendanceBase
from domain.administration_module.entity.Attendance import Attendance
from domain.sales_module.dto.schemaOrder import SchemaOrder, SchemaOrderByEmployeCreate, SchemaOrderByMesaCreate
from domain.sales_module.entity.Order import Order


class SaleService:
    def __init__(self, repository_order) -> None:
        self._repository_order = repository_order

    ################################################################### ORDER ####################################################
    # debo verificar que ellempleado que se asigna este presente
    def create_order_by_employe(self, order_data: SchemaOrderByEmployeCreate, query_asistence: SchemaAttendanceBase):
        logging.warning("creando nueva orden")
        new_order = Order(**order_data.__dict__)
        logging.warning(query_asistence)

        # Verifica si hay alguna asistencia con 'presente' igual a True y el 'empleado_id' coincidente

        if query_asistence.presente == True:

            self._repository_order.create(new_order)
            return new_order
        else:
            # Si no se encontró ninguna asistencia presente que coincida, genera un mensaje de error
            raise Exception("El empleado no está presente")

    def create_order_by_mesa(self, order_data: SchemaOrderByMesaCreate):
        new_order = Order(**order_data.__dict__)
        self._repository_order.create(new_order)
        return new_order

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        logging.warning("entrando al repositorio")
        order = self._repository_order.get_by_id(order_id)
        return order

    def get_all_orders(self) -> List[Order]:
        orders = self._repository_order.get_all()
        return orders

    def update_order(self, order_data: SchemaOrder):
        self._repository_order.update(order_data)
        return None

    def delete_order(self, order_id: int) -> None:
        return self._repository_order.delete_by_id(order_id)
