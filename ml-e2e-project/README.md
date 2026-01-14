# Proyecto End-to-End de Machine Learning

Este repositorio contiene el código y la configuración para un proyecto de ML completo, desde el frontend hasta el despliegue en Kubernetes.

## Estructura del Proyecto

- `frontend/`: Aplicación de cara al usuario (ej. React).
- `backend/`: API de negocio que consume el servicio de inferencia.
- `inference-service/`: API dedicada a la inferencia del modelo de ML.
- `k8s/`: Manifiestos de Kubernetes para el despliegue en producción.
- `docker-compose.yml`: Para orquestar los servicios en un entorno de desarrollo local.
- `README.md`: Este archivo.
- `docs/`: Documentación técnica y de arquitectura.

## Desarrollo Local

1. **Levantar todos los servicios:**
   ```bash
   docker-compose up --build
   ```

2. **Acceder a los servicios:**
   - **Frontend:** [http://localhost:3000](http://localhost:3000)
   - **Backend API:** [http://localhost:8080](http://localhost:8080)
   - **Inference API:** [http://localhost:8000/docs](http://localhost:8000/docs)

## Despliegue en Kubernetes

1. **Construir y subir las imágenes a un registro (ej. Docker Hub, GCR):**
   ```bash
   docker build -t your-registry/frontend:latest ./frontend
   docker push your-registry/frontend:latest
   # Repetir para backend e inference-service
   ```

2. **Aplicar los manifiestos de Kubernetes:**
   ```bash
   kubectl apply -f k8s/
   ```

## Documentación
- Frontend: [docs/frontend.md](file:///d:/GitHub/Guia_docker/ml-e2e-project/docs/frontend.md)
- Backend: [docs/backend.md](file:///d:/GitHub/Guia_docker/ml-e2e-project/docs/backend.md)
- Inference Service: [docs/inference-service.md](file:///d:/GitHub/Guia_docker/ml-e2e-project/docs/inference-service.md)
- Kubernetes: [docs/k8s.md](file:///d:/GitHub/Guia_docker/ml-e2e-project/docs/k8s.md)
- Docker/Compose: [docs/docker.md](file:///d:/GitHub/Guia_docker/ml-e2e-project/docs/docker.md)
