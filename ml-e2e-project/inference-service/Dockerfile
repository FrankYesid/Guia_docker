FROM python:3.9-slim

WORKDIR /app

# Copiar requirements desde el directorio padre (contexto de build)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY ./app /app/app
# Copiar directorio de modelos (si existe)
COPY ./models /app/models

EXPOSE 8000

# Ejecutar desde el directorio /app pero apuntando al módulo app.main
# PYTHONPATH se ajusta automáticamente o podemos ser explícitos.
# Aquí asumimos que uvicorn buscará en el path actual.
ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
