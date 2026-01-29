# Imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de la aplicación
COPY aplicacion.py .

# Comando para ejecutar la aplicación de forma interactiva
CMD ["python", "-u", "app.py"]
