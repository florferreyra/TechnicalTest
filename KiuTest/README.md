# KIU TEST PROJECT

This project is using Python 3.9 with FastAPi.
This README provides instructions on how to set up and run a Dockerized FastAPI project. 
The project does not include a frontend but utilizes OpenAPI to display its API documentation. 
To test the APIs, tools like Postman are recommended, and the necessary JSON for running Postman is provided in the email.

## Table of Contents

1. [Getting Started](#getting-started)
2. [API Endpoints](#api-endpoints)
3. [Testing the APIs](#testing-the-apis)
4. [Running Tests](#running-tests)

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- Docker
- Docker Compose

### Setup and Run

Build and start the Docker containers:
   ```bash 
     docker-compose up --build
   ```

3. Once the containers are running, the FastAPI server should be accessible at `http://localhost:8080`.

4. Access the API documentation at:
    - Swagger UI: `http://localhost:8080/docs`
    - ReDoc: `http://localhost:8080/redoc`

## API Endpoints

The main flow for achieving the required results involves the following steps:

1. **Create a Client**: Use the `/clients/` API to create a new client.
    - Method: `POST`
    - Example request body:
      ```json
      {
          "name": "Client Name"
      }
      ```

2. **Create a Cargo**: Use the `/cargos/` API to create a new cargo.
    - Method: `POST`
    - Example request body:
      ```json
      {
          "client_id": 1,
          "origin": "Cordoba",
          "destination": "Buenos Aires",
          "date": "2024-06-18"
      }
      ```

3. **Get Cargos by Date**: Use the `/cargos/?date={DATE}` API to get the total amount and number of cargos for a specific date.
    - Method: `GET`
    - URL parameter: `date` (format: `YYYY-MM-DD`)

## Testing the APIs

To test the APIs, you can use Postman. Import the provided Postman collection JSON to simplify the testing process.

1. Open Postman.
2. Import the JSON file:
    - Go to `File` -> `Import`.
    - Select the provided `postman_collection.json` file.
3. Use the imported collection to test the endpoints as described in the API Endpoints section.

## Running Tests

The project includes tests that are executed using `pytest`. Follow the steps below to run the tests:

1. Enter the API container:
    ```bash
    docker-compose exec api bash
    ```

2. Navigate to the `/app` directory:
    ```bash
    cd /app
    ```

3. Run the tests with `pytest`:
    ```bash
    pytest
    ```

## Conclusion

By following the above instructions, you should be able to set up and run the KiuTest project, test its APIs, and run the provided tests.
