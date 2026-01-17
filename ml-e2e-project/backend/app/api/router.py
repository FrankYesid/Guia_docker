from fastapi import APIRouter
from app.core.config import settings
from app.services.inference_client import InferenceClient
from app.models.schemas import UserInput, PredictionResult

router = APIRouter()
client = InferenceClient()

@router.get("/")
def health():
    return {
        "status": "ok",
        "inference_service_url": settings.inference_service_url,
    }

@router.post("/process-prediction", response_model=PredictionResult)
def process_prediction(data: UserInput) -> PredictionResult:
    resp = client.predict(data.dict())
    return PredictionResult(
        input_summary=f"F1: {data.feature1}, F2: {data.feature2}",
        prediction_raw=float(resp["prediction"]),
    )
