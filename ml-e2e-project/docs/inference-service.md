# Documentación del Servicio de Inferencia

Servicio HTTP que carga un artefacto de modelo (o entrena uno simple si falta) y expone predicciones.

## Overview
- Framework: FastAPI
- Puerto: 8000
- Dependencias: ver [requirements.txt](file:///d:/GitHub/Guia_docker/ml-e2e-project/inference-service/requirements.txt)
- Código principal: [main.py](file:///d:/GitHub/Guia_docker/ml-e2e-project/inference-service/app/main.py)
- Docker: [Dockerfile](file:///d:/GitHub/Guia_docker/ml-e2e-project/inference-service/Dockerfile)
- Modelos: carpeta [models](file:///d:/GitHub/Guia_docker/ml-e2e-project/inference-service/models)

## Endpoints
- GET `/`  
  Estado del servicio y indicador `model_loaded`.
- POST `/predict`  
  Entrada:
  ```json
  { "feature1": 1.0, "feature2": 2.0, "feature3": 3.0 }
  ```
  Salida:
  ```json
  { "prediction": 4.0 }
  ```

## Carga de Modelo
- Ruta de artefacto: `models/model.pkl`
- Si no existe, se entrena un **LinearRegression** mínimo para mantener operativa la API. Ver [main.py](file:///d:/GitHub/Guia_docker/ml-e2e-project/inference-service/app/main.py#L23-L33)

## Ejecución
### Local (sin Docker)
```bash
pip install -r inference-service/requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Docker
```bash
docker build -t ml-inference:latest ./inference-service
docker run -p 8000:8000 -v $(pwd)/inference-service/models:/app/models ml-inference:latest
```

