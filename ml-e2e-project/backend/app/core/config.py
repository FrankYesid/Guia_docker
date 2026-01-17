from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Backend Business API"
    inference_service_url: str = "http://inference-service:8000"
    request_timeout_seconds: int = 5
    log_level: str = "INFO"

    class Config:
        case_sensitive = False

settings = Settings()
