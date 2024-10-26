# Usa una imagen base de Python
FROM python:3.8

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el contenido del proyecto al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install -r requirements.txt

# Expone el puerto que usará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
