#Imagen base
FROM python:3.6 

#Redirigimos al directorio app
WORKDIR /app

#Copiamos todo el contenido actual
COPY . /app

#Instalar las librerias adicionales
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#Habilita el puerto
EXPOSE 80

ENV NAME World

CMD ["python", "turnos-medicos-service-flask/main.py"]