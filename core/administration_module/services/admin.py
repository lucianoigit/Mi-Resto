import logging
import traceback
from typing import List, Optional
from fastapi import Depends
from domain.administration_module.dto.schemaAsist import SchemaAttendanceCreate
from domain.administration_module.dto.schemaEmployee import SchemaEmployee, SchemaEmployeeCreate
from domain.administration_module.entity.Attendance import Attendance
from domain.administration_module.entity.Employee import Empleado
from domain.administration_module.entity.modelRol import Rol
from domain.administration_module.dto.schemaRol import SchemaRolCreate


class AdminService:
    def __init__(self, repository_rol, repository_empleado, repository_asist) -> None:
        self._repository_rol = repository_rol
        self._repository_empleado = repository_empleado
        self._repository_asist = repository_asist
    ################################################################### ROLES ####################################################

    def create_rol(self, rol_data: SchemaRolCreate):
        new_rol = Rol(**rol_data.__dict__)
        logging.warning("accediendo al servicio")
        self._repository_rol.create(new_rol)
        return new_rol

    def get_rol_by_id(self, rol_id: int) -> Optional[Rol]:
        logging.warning("entrando al repositorio")
        rol = self._repository_rol.get_by_id(rol_id)
        return rol

    def get_all_rols(self) -> List[Rol]:
        rols = self._repository_rol.get_all()
        return list(rols)

    def delete_rol(self, rol_id: int) -> None:
        return self._repository_rol.delete_by_id(rol_id)

    ################################################################### EMPLEADOS ####################################################

    def create_empleado(self, empleado_data: SchemaEmployeeCreate):
        new_empleado = Empleado(**empleado_data.__dict__)
        logging.warning("accediendo al servicio")
        self._repository_empleado.create(new_empleado)
        return new_empleado

    def get_empleado_by_id(self, empleado_id: int) -> Optional[Empleado]:
        logging.warning("entrando al repositorio")
        empleado = self._repository_empleado.get_by_id(empleado_id)
        return empleado

    def get_all_empleados(self) -> List[Empleado]:
        empleados = self._repository_empleado.get_all()
        return empleados

    def delete_empleado(self, empleado_id: int) -> None:
        return self._repository_empleado.delete_by_id(empleado_id)

    def create_asistence(self, asistencia_data: SchemaAttendanceCreate):
        empleado_asist = Attendance(**asistencia_data.__dict__)
        self._repository_asist.create(empleado_asist)
        return empleado_asist

    def get_asistence_by_id(self, asistence_id: int) -> Optional[Attendance]:
        asistencia = self._repository_asist.get_by_id(asistence_id)
        return asistencia

    def deleted_asistence(self, asist_id: int) -> None:
        return self._repository_asist.delete(asist_id)

    def get_all_empleados_asist(self) -> List[Attendance]:
        asistencias = self._repository_asist.get_all()
        return list(asistencias)

    def asing_rol(self, empleado_id: int, rol_id: int):
        try:
            empleado = self.get_empleado_by_id(empleado_id)

            if not empleado:

                print("Empleado no encontrado. ID:", empleado_id)
                return {
                    "error": "Empleado no encontrado"
                }

            rol = self.get_rol_by_id(rol_id)

            if not rol:
                # Agrega registros de depuración
                print("Rol no encontrado. ID:", rol_id)
                return {
                    "error": "Rol no encontrado"
                }

            empleado.rol_id = rol.id

            try:
                self._repository_empleado.update(empleado)

                print("Actualización exitosa")
                return {

                    "asignacion ejecutada con exito"
                }
            except Exception as e:

                error_message = f"Error al asignar rol: {str(e)}"
                traceback.print_exc()
                return {
                    "error": error_message
                }

        except Exception as e:

            error_message = f"Error general: {str(e)}"
            traceback.print_exc()
            return {
                "error": error_message
            }

    ################################################################### MESAS ####################################################
