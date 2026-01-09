# 1. Usar una imagen base oficial y ligera de Python
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar solo el archivo de dependencias para aprovechar la caché de Docker
# Esto acelera las builds si las dependencias no cambian.
COPY app/requirements.txt .

# 4. Instalar las dependencias de Python
# --no-cache-dir reduce el tamaño de la imagen al no almacenar la caché de pip.
# --upgrade pip asegura que estamos usando una versión reciente de pip.
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# 5. Copiar el resto del código de la aplicación al directorio de trabajo
COPY ./app /app
COPY ./models /app/models

# 6. Exponer el puerto en el que la aplicación se ejecutará dentro del contenedor
EXPOSE 8000

# 7. Comando para ejecutar la aplicación cuando se inicie el contenedor
# uvicorn: el servidor ASGI.
# main:app: el objeto 'app' de FastAPI en el archivo 'main.py'.
# --host 0.0.0.0: hace que el servidor sea accesible desde fuera del contenedor.
# --port 8000: el puerto en el que escuchar.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
