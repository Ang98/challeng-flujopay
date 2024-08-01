# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos y el código fuente al contenedor
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY clientes.json clientes.json
COPY static/ static/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
