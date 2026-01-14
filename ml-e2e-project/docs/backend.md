# Documentación del Backend

Esta guía describe el Backend del proyecto E2E de ML: endpoints, configuración, dependencias e integración con el servicio de inferencia.

## Overview
- Framework: FastAPI
- Puerto: 8080
- Dependencias: ver [requirements.txt](file:///d:/GitHub/Guia_docker/ml-e2e-project/backend/requirements.txt)
- Código principal: [main.py](file:///d:/GitHub/Guia_docker/ml-e2e-project/backend/app/main.py)
- Docker: [Dockerfile](file:///d:/GitHub/Guia_docker/ml-e2e-project/backend/Dockerfile)

## Endpoints
- GET `/`  
  Estado del servicio y URL del inferencia.
- POST `/process-prediction`  
  Entrada:
  ```json
  { "feature1": 1.0, "feature2": 2.0, "feature3": 3.0 }
  ```
  Salida:
  ```json
  { "input_summary": "F1: 1.0, F2: 2.0", "prediction_raw": 4.0, "status": "completed" }
  ```

## Configuración
- Variable de entorno: `INFERENCE_SERVICE_URL`  
  - Compose: `http://inference-service:8000`  
  - K8s Service: `http://inference-service`

## Ejecución
### Local (sin Docker)
```bash
pip install -r backend/requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

### Docker
```bash
docker build -t ml-backend:latest ./backend
docker run -p 8080:8080 -e INFERENCE_SERVICE_URL=http://localhost:8000 ml-backend:latest
```

## Integración
- Llama al endpoint `/predict` del inferencia: ver [main.py](file:///d:/GitHub/Guia_docker/ml-e2e-project/backend/app/main.py#L34-L41)

