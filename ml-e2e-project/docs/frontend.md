# Documentación del Frontend (ML Prediction Dashboard)

Este documento detalla la arquitectura, desarrollo y despliegue del componente Frontend de nuestro sistema End-to-End de Machine Learning.

## 1. Descripción General

El Frontend es una aplicación **Single Page Application (SPA)** construida con **React**. Su objetivo principal es proporcionar una interfaz intuitiva para que los usuarios finales interactúen con el modelo de Machine Learning sin necesidad de conocimientos técnicos.

### Tecnologías Clave:
- **React 18:** Librería de UI para construir componentes interactivos.
- **Axios:** Cliente HTTP para comunicarse con el Backend API.
- **Nginx:** Servidor web de alto rendimiento utilizado para servir los archivos estáticos en producción.
- **Docker:** Contenerización multi-etapa para optimizar el tamaño de la imagen final.

## 2. Estructura del Proyecto

```
frontend/
├── public/              # Archivos estáticos públicos
│   └── index.html       # Punto de entrada HTML
├── src/                 # Código fuente de React
│   ├── App.js           # Componente principal y lógica de estado
│   ├── App.css          # Estilos CSS
│   ├── index.js         # Punto de montaje de React
│   └── index.css        # Estilos globales
├── nginx/
│   └── nginx.conf       # Configuración de servidor para producción
├── Dockerfile           # Definición de construcción y despliegue
└── package.json         # Dependencias y scripts
```

## 3. Flujo de Comunicación

1.  **Entrada de Usuario:** El usuario ingresa los valores de las características (`feature1`, `feature2`, `feature3`) en el formulario.
2.  **Solicitud HTTP:** Al hacer clic en "Predecir", Axios envía una solicitud POST al Backend.
    *   **Desarrollo Local:** `http://localhost:8080/process-prediction`
    *   **Producción (K8s):** El Ingress redirige las peticiones de `/api` al servicio de Backend.
3.  **Respuesta:** La aplicación recibe la predicción JSON y actualiza el estado para mostrar el resultado en pantalla.

## 4. Desarrollo Local

Para ejecutar el frontend en modo desarrollo (con hot-reload):

1.  Asegúrate de tener Node.js instalado.
2.  Instala las dependencias:
    ```bash
    cd frontend
    npm install
    ```
3.  Inicia el servidor de desarrollo:
    ```bash
    npm start
    ```
    La aplicación estará disponible en `http://localhost:3000`.

**Nota:** Asegúrate de que el Backend esté corriendo en el puerto 8080 para que las peticiones funcionen.

## 5. Construcción con Docker (Producción)

Utilizamos un **Dockerfile Multi-Stage** para garantizar una imagen final ligera y segura.

### Etapa 1: Build (Node.js)
Compila el código React (JSX, ES6) a archivos estáticos (HTML, CSS, JS minificado) en la carpeta `/build`.

### Etapa 2: Serve (Nginx Alpine)
Toma solo los archivos de la carpeta `/build` de la etapa anterior y los sirve utilizando Nginx sobre una imagen Alpine Linux mínima.

### Comandos:
```bash
# Construir la imagen
docker build -t ml-frontend:latest .

# Ejecutar el contenedor
docker run -p 3000:80 ml-frontend:latest
```

## 6. Configuración de Nginx

El archivo `nginx.conf` está configurado para manejar el enrutamiento de una SPA. Específicamente, la directiva `try_files $uri $uri/ /index.html;` asegura que si un usuario recarga la página en una ruta profunda (ej. `/resultados`), Nginx sirva el `index.html` para que React Router (si se implementara en el futuro) maneje la ruta en el cliente, evitando errores 404.
