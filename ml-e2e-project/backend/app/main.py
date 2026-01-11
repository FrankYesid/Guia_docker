from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="Backend Business API", version="1.0.0")

# URL del servicio de inferencia
# En Docker Compose: http://inference-service:8000
# En Kubernetes: http://inference-service
INFERENCE_SERVICE_URL = os.getenv("INFERENCE_SERVICE_URL", "http://inference-service:8000")

class UserInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.get("/")
def read_root():
    return {
        "message": "Backend API is active",
        "inference_service_url": INFERENCE_SERVICE_URL
    }

@app.post("/process-prediction")
def process_prediction(data: UserInput):
    """
    Recibe datos del usuario, valida, y llama al servicio de inferencia.
    """
    try:
        # 1. Validación o lógica de negocio previa
        print(f"Procesando petición para: {data}")

        # 2. Llamada al servicio de inferencia
        predict_url = f"{INFERENCE_SERVICE_URL}/predict"
        # Enviamos los datos como dict, requests lo convierte a JSON
        response = requests.post(predict_url, json=data.dict(), timeout=5)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error en servicio de inferencia")
            
        prediction_result = response.json()
        
        # 3. Lógica post-predicción (ej. formateo, guardado en DB)
        result = {
            "input_summary": f"F1: {data.feature1}, F2: {data.feature2}",
            "prediction_raw": prediction_result["prediction"],
            "status": "completed"
        }
        
        return result

    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="No se pudo conectar con el servicio de inferencia")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
