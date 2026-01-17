import requests
from fastapi import HTTPException
from app.core.config import settings
from app.core.logging import logger

class InferenceClient:
    def __init__(self, base_url: str | None = None, timeout_seconds: int | None = None):
        self.base_url = base_url or settings.inference_service_url
        self.timeout = timeout_seconds or settings.request_timeout_seconds

    def predict(self, payload: dict) -> dict:
        url = f"{self.base_url}/predict"
        logger.debug(f"Llamando inferencia en {url} con payload {payload}")
        try:
            resp = requests.post(url, json=payload, timeout=self.timeout)
            if resp.status_code != 200:
                raise HTTPException(status_code=resp.status_code, detail="Error en servicio de inferencia")
            return resp.json()
        except requests.exceptions.ConnectionError:
            raise HTTPException(status_code=503, detail="No se pudo conectar con el servicio de inferencia")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
