# Mi-Resto: CRUD App

Este proyecto es una plantilla inicial de **arquitectura limpia** implementada con **FastAPI**. Está diseñado para servir como base para proyectos modulares y escalables, proporcionando una separación clara de responsabilidades y capas.

## Estructura del Proyecto

El proyecto sigue los principios de la arquitectura limpia, con las siguientes carpetas principales:

- **`abstract`**: Define interfaces y contratos entre las capas.
- **`catalog_module`**: Módulos específicos del dominio, como catálogos o funcionalidades relacionadas.
- **`container`**: Configuración del contenedor de dependencias para inyección de servicios.
- **`core`**: Contiene la lógica central y elementos transversales al proyecto.
- **`db`**: Configuración y manejo de la base de datos.
- **`domain`**: Define las entidades del dominio y reglas de negocio.
- **`repositories`**: Implementaciones específicas para la persistencia de datos.

### Archivos Clave

- **`main.py`**: Punto de entrada de la aplicación. Configura los endpoints de FastAPI y las rutas principales.
- **`requerimientos.txt`**: Lista de dependencias necesarias para ejecutar el proyecto.

---

## Instalación y Configuración

### Requisitos Previos

- **Python 3.9+**
- Administrador de paquetes: **pip**
- Base de datos compatible (PostgreSQL, MySQL, SQLite, etc.)

### Instrucciones

1. **Clonar el Repositorio**
   ```bash
   git clone <URL-del-repositorio>
   cd Mi-Resto
   ```

2. **Crear un Entorno Virtual**
   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows: .\env\Scripts\activate
   ```

3. **Instalar Dependencias**
   ```bash
   pip install -r requerimientos.txt
   ```

4. **Configurar la Base de Datos**
   - Configura las variables de entorno necesarias para la conexión a la base de datos (por ejemplo, URL de conexión, usuario, contraseña).

5. **Ejecutar Migraciones** (opcional si usas una herramienta como Alembic)
   ```bash
   alembic upgrade head
   ```

6. **Iniciar el Servidor**
   ```bash
   uvicorn main:app --reload
   ```
   El servidor estará disponible en: `http://127.0.0.1:8000`

---

## Características

1. **Arquitectura Modular**
   - Separación clara entre dominio, infraestructura y aplicación.
   - Facilidad para extender o modificar componentes sin afectar otras partes del sistema.

2. **FastAPI**
   - Framework ligero y moderno para construir APIs RESTful.
   - Soporte integrado para OpenAPI y documentación automática.

3. **Inyección de Dependencias**
   - Uso de contenedores para gestionar dependencias y facilitar pruebas unitarias.

4. **Soporte para Base de Datos**
   - Implementación de repositorios para el manejo de datos.
   - Soporte para diferentes motores de base de datos.

5. **Extensibilidad**
   - Plantilla diseñada para agregar nuevos módulos y funcionalidades rápidamente.

---





