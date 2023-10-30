from typing import List
from domain.administration_module.entity.Attendance import Attendance
from domain.administration_module.entity.Employee import Empleado
from domain.sales_module.dto.schemaOrder import SchemaOrderByMesaCreate
from domain.sales_module.entity.Order import Order


class AsingEmployeService:
    def __init__(self, repository_order, repository_empleado, repository_asist) -> None:
        self._repository_order = repository_order
        self._repository_empleado = repository_empleado
        self._repository_asist = repository_asist

    def asing_employe(self, empleados_asist: List[Attendance], order_id: int):
        # Obtener el empleado y la mesa de la base de datos
        empleado_with_least_orders = None
        least_order_count = float('inf')
        for empleado in empleados_asist:
            if empleado.presente == True:
                order_query = self._repository_order.get_all().filter(
                    Order.empleado_id == empleado.id).count()
                if order_query < least_order_count:
                    least_order_count = order_query
                    empleado_with_least_orders = empleado

        order = self._repository_order.get_by_id(order_id)
        order.empleado_id = empleado_with_least_orders.id
        self._repository_order.update(order)
