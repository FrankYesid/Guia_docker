# Guía de Docker y Docker Compose

Instrucciones para construir y ejecutar los servicios del proyecto en contenedores.

## Imágenes y Dockerfiles
- Frontend: [Dockerfile](file:///d:/GitHub/Guia_docker/ml-e2e-project/frontend/Dockerfile) (multi-stage con Nginx)
- Backend: [Dockerfile](file:///d:/GitHub/Guia_docker/ml-e2e-project/backend/Dockerfile)
- Inference: [Dockerfile](file:///d:/GitHub/Guia_docker/ml-e2e-project/inference-service/Dockerfile)

## Desarrollo Local con Compose
Archivo: [docker-compose.yml](file:///d:/GitHub/Guia_docker/ml-e2e-project/docker-compose.yml)

### Levantar servicios
```bash
docker-compose up --build
```

### Servicios y puertos
- Frontend: http://localhost:3000
- Backend: http://localhost:8080
- Inference: http://localhost:8000/docs

### Dependencias entre servicios
- `backend` depende de `inference-service`  
  Ver variable `INFERENCE_SERVICE_URL` en compose.

## Build manual de cada servicio
```bash
# Frontend
docker build -t ml-frontend:latest ./frontend
# Backend
docker build -t ml-backend:latest ./backend
# Inference
docker build -t ml-inference:latest ./inference-service
```

