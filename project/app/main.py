# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Cargar el modelo al iniciar la aplicación
# En un caso real, asegúrate de que la ruta al modelo es correcta dentro del contenedor.
try:
    model = joblib.load("models/model.pkl")
except FileNotFoundError:
    # En un entorno real, aquí deberías tener un manejo de errores más robusto.
    # Por ahora, creamos un placeholder si el modelo no existe.
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    print("Advertencia: No se encontró 'models/model.pkl'. Usando un modelo placeholder.")


app = FastAPI(title="API de Inferencia de ML", version="1.0.0")

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

class OutputData(BaseModel):
    prediction: float


@app.get("/", summary="Endpoint de estado", description="Verifica si la API está en funcionamiento.")
def read_root():
    return {"status": "API de inferencia funcionando correctamente."}


@app.post("/predict", response_model=OutputData, summary="Realizar una predicción", description="Recibe datos de entrada y devuelve una predicción del modelo.")
def predict(data: InputData):
    """
    Realiza una predicción utilizando el modelo de Machine Learning cargado.
    - **feature1**: Primera característica para la predicción.
    - **feature2**: Segunda característica para la predicción.
    - **feature3**: Tercera característica para la predicción.
    """
    # El modelo espera una entrada 2D, por eso el doble corchete.
    prediction_value = model.predict([[data.feature1, data.feature2, data.feature3]])
    
    # La predicción es un array, extraemos el primer elemento.
    return {"prediction": prediction_value[0]}
