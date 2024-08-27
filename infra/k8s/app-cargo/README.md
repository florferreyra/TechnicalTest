# PROJECTO CARGO

Este proyecto utiliza Python 3.9 con FastAPI.
Este README proporciona instrucciones sobre cómo configurar y ejecutar un proyecto de FastAPI utilizando Docker.
El proyecto no incluye una interfaz frontend, pero utiliza OpenAPI para mostrar la documentación de su API.
Para probar las APIs, se recomiendan herramientas como Postman.

## Tabla de Contenidos

1. [Primeros Pasos](#primeros-pasos)
2. [Endpoints de la API](#endpoints-de-la-api)

4. [Ejecución de tests](#ejecucion-de-tests)

## Primeros Pasos

### Requisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:
- Docker
- Docker Compose

### Configuración y Ejecución

Construye y levanta los contenedores de Docker:
   ```bash 
     docker-compose up --build
   ```

3. Una vez que los contenedores estén en funcionamiento, el servidor FastAPI debería estar accesible en `http://localhost:8080`.

4. Accede a la documentación de la API en:
    - Swagger UI: `http://localhost:8080/docs`
    - ReDoc: `http://localhost:8080/redoc`

## Endpoints de la API

El flujo principal para lograr los resultados requeridos implica los siguientes pasos:

1. **Crear un Cliente**: Usa la API `/clients/` para crear un nuevo cliente.
    - Metodo: `POST`
    - Ejemplo del cuerpo de la solicitud:
      ```json
      {
          "name": "Client Name"
      }
      ```

2. **Crear un Cargo**: Usa la API `/cargos/` para crear un nuevo cargo.
    - Metodo: `POST`
    - Ejemplo del cuerpo de la solicitud:
      ```json
      {
          "client_id": 1,
          "origin": "Cordoba",
          "destination": "Buenos Aires",
          "date": "2024-06-18"
      }
      ```

3. **Obtener Cargos por Fecha**: Usa la API `/cargos/?date={DATE}` para obtener la cantidad total y el número de cargos para una fecha específica. 
    - Metodo: `GET`
    - Parámetro de la URL: `date` (formato: `YYYY-MM-DD`)

## Ejecucion de Tests

El proyecto incluye pruebas que se ejecutan utilizando pytest. Sigue los pasos a continuación para ejecutar las pruebas:

1. Ingresa al contenedor de la API:
    ```bash
    docker-compose exec api bash
    ```

2. Navega al directorio /app:
    ```bash
    cd /app
    ```

3. Ejecuta las pruebas con pytest:
    ```bash
    pytest
    ```

## Conclusión

Siguiendo las instrucciones anteriores, deberías poder configurar y ejecutar el proyecto CargoApp, probar sus APIs y ejecutar las pruebas proporcionadas.
