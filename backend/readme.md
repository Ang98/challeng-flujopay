# Cliente API con Flask

Este proyecto es una API RESTful construida con Flask que permite realizar operaciones CRUD sobre un recurso de cliente. La API incluye autenticación JWT para asegurar el acceso a los endpoints y Swagger para la documentación de la API.

## Características

- **CRUD de Clientes**: Crear, Leer, Actualizar y Eliminar clientes.
- **Autenticación JWT**: Protege los endpoints con autenticación basada en tokens.
- **Documentación Swagger**: Proporciona una interfaz interactiva para explorar y probar la API.

## Estructura del Proyecto

- `app.py`: Código principal de la aplicación Flask.
- `clientes.json`: Archivo JSON que almacena los datos de los clientes.
- `static/swagger.json`: Archivo de configuración Swagger para la documentación de la API.
- `Dockerfile`: Configuración para construir la imagen Docker.
- `docker-compose.yml`: Configuración para gestionar los servicios Docker.
- `requirements.txt`: Archivo de dependencias del proyecto.

## Instalación y Ejecución

### Requisitos

- Docker y Docker Compose deben estar instalados en tu máquina.

### Construir y Ejecutar

1. **Construir la imagen Docker**:

   ```sh
   docker-compose build
