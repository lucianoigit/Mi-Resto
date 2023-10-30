from domain.administration_module.dto.schemaMesa import *
from domain.administration_module.entity.mesa import Mesa


class MesaService:
    def __init__(self, repository_mesa, repository_empleado, repository_asist) -> None:
        self._repository_mesa = repository_mesa
        self._repository_empleado = repository_empleado
        self._repository_asist = repository_asist

    def create_mesa(self, mesa_data: SchemaMesaCreate):
        new_mesa = Mesa(**mesa_data.__dict__)
        self._repository_mesa.create(new_mesa)
        return new_mesa

    def get_mesa_by_id(self, mesa_id: int):
        mesa = self._repository_mesa.get_by_id(mesa_id)
        return mesa

    def get_all_mesa(self):
        mesas = self._repository_mesa.get_all()
        return mesas

    def update_mesa(self, mesa_data: SchemaMesaCreate):
        self._repository_mesa.update(mesa_data)
        return None

    def delete_mesa(self, mesa_id: int):
        self._repository_mesa.delete_by_id(mesa_id)

    def asing_order(self, empleado_id: int, mesa_id: int, asistencias: bool):
        # Obtener el empleado y la mesa de la base de datos
        empleado = self._repository_empleado.get_by_id(empleado_id)
        mesa = self._repository_mesa.get_by_id(mesa_id)
        if asistencias == True:

            # Verificar si el empleado y la mesa existen
            if not empleado or not mesa:
                return None  # Manejar este caso según tus necesidades, por ejemplo, lanzar una excepción

        # Realizar la asignación del empleado a la mesa
            empleado.mesas.append(mesa)  # Asignar la mesa al empleado

        # Aquí puedes realizar otras acciones, como manejar las asistencias si es necesario
        # asistencias es un dato adicional que puedes procesar aquí

        # Guardar los cambios en la base de datos
            self._repository_empleado.modificar(empleado)

            return empleado  # Opcional: Puedes devolver el empleado actualizado si lo necesitas
