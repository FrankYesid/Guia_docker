# Documentación de Kubernetes (Despliegue E2E)

Manifiestos y flujo de enrutamiento para Backend, Servicio de Inferencia y Frontend.

## Archivos
- Backend: [backend.yaml](file:///d:/GitHub/Guia_docker/ml-e2e-project/k8s/backend.yaml)
- Inference: [inference-service.yaml](file:///d:/GitHub/Guia_docker/ml-e2e-project/k8s/inference-service.yaml)
- Ingress: [ingress.yaml](file:///d:/GitHub/Guia_docker/ml-e2e-project/k8s/ingress.yaml)

## Componentes
- **Deployment**: define réplicas, imagen y recursos de cada servicio.
- **Service (ClusterIP)**: DNS estable interno para acceder a Pods.
- **Ingress**: expone HTTP/HTTPS y enruta a servicios internos.

## Flujo
1. Usuario → Ingress (`host`/ruta)
2. Ingress → `backend-service`
3. Backend → `inference-service`
4. Respuesta → Backend → Ingress → Usuario

## Despliegue
```bash
kubectl apply -f k8s/
kubectl get deployments,svc,ingress
```

## Ajustes Clave
- Reemplazar las imágenes `your-docker-registry/*` por imágenes propias.
- Configurar `host` del Ingress y TLS si corresponde.
- Escalado: ajustar `replicas` y `resources` según carga.

