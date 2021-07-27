FROM python:3.7
RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt
RUN pip install -U flask-cors
RUN pip install flasgger
COPY . .