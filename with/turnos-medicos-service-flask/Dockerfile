FROM python:3.6-alpine3.10

WORKDIR /turnos-medicos-service-flask

COPY requirements.txt /turnos-medicos-service-flask
RUN pip install -r requirements.txt
RUN apk update

COPY main.py /turnos-medicos-service-flask
COPY helper.py /turnos-medicos-service-flask

ENV HOST=0.0.0.0

EXPOSE 5000

CMD python main.py