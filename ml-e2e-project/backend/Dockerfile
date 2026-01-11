FROM python:3.9-slim

WORKDIR /app

# Copiar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY ./app /app/app

EXPOSE 8080

ENV PYTHONPATH=/app

# El backend corre en el puerto 8080 según definimos en k8s/backend.yaml y docker-compose.yml
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
