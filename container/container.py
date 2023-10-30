import logging
from typing import TypeVar
from dependency_injector import containers, providers
from core.administration_module.services.admin import AdminService
from core.administration_module.services.asingEmploye import AsingEmployeService
from core.administration_module.services.mesa import MesaService

from db.database import Base, Database
from domain.administration_module.entity.Attendance import Attendance
from domain.administration_module.entity.Employee import Empleado
from domain.administration_module.entity.mesa import Mesa
from domain.administration_module.entity.modelRol import Rol
from repositories.GenericMySQLRepository import GenericMySQLRepository
from domain.sales_module.entity.Order import Order
from core.sales_module.services.SaleService import SaleService


Model = TypeVar("Model", bound=Base)
logging.info("accediendo al contenedor")


class Container(containers.DeclarativeContainer):

    logging.info("accediendo al contenedor")

    wiring_config = containers.WiringConfiguration(modules=["core.administration_module.controllers.controllerRol",
                                                            "core.administration_module.controllers.controllerEmployee",
                                                            "core.administration_module.controllers.controllerAttendance",
                                                            "core.administration_module.controllers.controllerMesa",
                                                            "core.administration_module.controllers.asingEmploye",
                                                            "core.sales_module.controllers.controllerOrder"])

    db = providers.Singleton(
        Database, db_url='mysql+pymysql://root:irda0205@localhost/miresto')

    ################################################################### ADMINISTRATION MODULE ####################################################

    repository_rol_provider = providers.Factory(
        GenericMySQLRepository,
        session_factory=db.provided.session,
        entity_type=Rol
    )

    repository_empleado_provider = providers.Factory(
        GenericMySQLRepository,
        session_factory=db.provided.session,
        entity_type=Empleado
    )

    repository_asist_provider = providers.Factory(
        GenericMySQLRepository,
        session_factory=db.provided.session,
        entity_type=Attendance
    )

    repository_mesa_provider = providers.Factory(
        GenericMySQLRepository,
        session_factory=db.provided.session,
        entity_type=Mesa
    )

    service_admin_provider = providers.Resource(
        AdminService,
        repository_rol=repository_rol_provider,
        repository_empleado=repository_empleado_provider,
        repository_asist=repository_asist_provider
    )

    service_mesa_provider = providers.Resource(
        MesaService,
        repository_mesa=repository_mesa_provider,
        repository_empleado=repository_empleado_provider,
        repository_asist=repository_asist_provider
    )

    ################################################################### SALES MODULE ####################################################

    repository_order_provider = providers.Factory(
        GenericMySQLRepository,
        session_factory=db.provided.session,
        entity_type=Order
    )

    service_Sale_provider = providers.Resource(
        SaleService,
        repository_order=repository_order_provider,

    )

    service_orderEmploye_provider = providers.Resource(
        AsingEmployeService,
        repository_order=repository_order_provider,
        repository_empleado=repository_empleado_provider,
        repository_asist=repository_asist_provider
    )
