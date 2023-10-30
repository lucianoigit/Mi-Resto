import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from container.container import Container
from core.administration_module.controllers.controllerRol import router as controllerRolRouter
from core.administration_module.controllers.controllerEmployee import router as controllerEmployeeRouter
from core.administration_module.controllers.controllerAttendance import router as controllerAttendanceRouter
from core.administration_module.controllers.asingEmploye import router as controllerAsingEmployeRouter
from core.administration_module.controllers.controllerMesa import router as controllerMesaRouter
from core.sales_module.controllers.controllerOrder import router as controllerOrderRouter


def create_app() -> FastAPI:
    container = Container()
    db = container.db()
    db.create_database()
    app = FastAPI(debug=True)
    app.container = container
    app.include_router(controllerRolRouter)
    app.include_router(controllerEmployeeRouter)
    app.include_router(controllerAttendanceRouter)
    app.include_router(controllerMesaRouter)
    app.include_router(controllerAsingEmployeRouter)
    app.include_router(controllerOrderRouter)

    @app.exception_handler(HTTPException)
    async def custom_http_exception_handler(request, exc):
        return JSONResponse(content={"detail": exc.detail}, status_code=exc.status_code)

    return app


""" 
logging.debug("Este es un mensaje de depuración")
logging.info("Este es un mensaje informativo") """
logging.warning("Este es un mensaje desde el main")
""" logging.error("Este es un mensaje de error")
logging.critical("Este es un mensaje crítico") """

app = create_app()
