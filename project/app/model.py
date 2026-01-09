# Lógica de carga y uso del modelo
# En este ejemplo simple, el modelo se carga directamente en main.py.
# Para proyectos más complejos, podrías tener aquí funciones auxiliares
# para preprocesar datos o postprocesar las predicciones.

def preprocess_data(data):
    """
    Función de ejemplo para preprocesar datos antes de la inferencia.
    """
    # Aquí iría la lógica de preprocesamiento: escalado, codificación, etc.
    print("Preprocesando datos...")
    return data

def postprocess_prediction(prediction):
    """
    Función de ejemplo para postprocesar la salida del modelo.
    """
    # Aquí iría la lógica de postprocesamiento.
    print("Postprocesando predicción...")
    return prediction
