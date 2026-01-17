from pydantic import BaseModel

class UserInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float

class PredictionResult(BaseModel):
    input_summary: str
    prediction_raw: float
    status: str = "completed"
