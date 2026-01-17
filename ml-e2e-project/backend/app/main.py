from fastapi import FastAPI
from app.api.router import router
from app.core.config import settings
from app.core.logging import logger

app = FastAPI(title=settings.app_name, version="1.0.0")

app.include_router(router)

@app.on_event("startup")
def on_startup():
    logger.info(f"Arrancando {settings.app_name} con nivel de logs {settings.log_level}")
