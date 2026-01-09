# Proyecto de Ejemplo: API de Inferencia con Docker

Este proyecto demuestra cómo empaquetar una API de inferencia de Machine Learning simple usando Docker y Docker Compose.

## Estructura del Proyecto

- `app/`: Contiene el código fuente de la API (FastAPI).
- `models/`: Almacena los artefactos del modelo (ej. `model.pkl`).
- `Dockerfile`: Instrucciones para construir la imagen de Docker de la API.
- `docker-compose.yml`: Define los servicios para ejecutar la aplicación en un entorno local.
- `README.md`: Este archivo.

## Cómo Ejecutar

1. **Construir y levantar el contenedor:**
   ```bash
   docker-compose up --build
   ```

2. **Acceder a la API:**
   - **Documentación interactiva (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
   - **Endpoint de predicción (usando `curl`):**
     ```bash
     curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"feature1": 1, "feature2": 2, "feature3": 3}'
     ```

3. **Detener el contenedor:**
   ```bash
   docker-compose down
   ```
