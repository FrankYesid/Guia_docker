from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI(title="Inference Service", version="1.0.0")

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

# Simulación de carga de modelo
MODEL_PATH = "models/model.pkl"
model = None

@app.on_event("startup")
def load_model():
    global model
    try:
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
            print(f"Modelo cargado desde {MODEL_PATH}")
        else:
            print("Modelo no encontrado, entrenando modelo dummy...")
            # Entrenar un modelo dummy simple para que el servicio funcione
            X = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
            y = np.array([2, 4, 6])
            model = LinearRegression()
            model.fit(X, y)
    except Exception as e:
        print(f"Error cargando modelo: {e}")

@app.get("/")
def health_check():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict")
def predict(data: InputData):
    if not model:
        return {"error": "Model not loaded"}
    
    # Predicción simple
    input_features = [[data.feature1, data.feature2, data.feature3]]
    prediction = model.predict(input_features)
    
    return {"prediction": float(prediction[0])}
 