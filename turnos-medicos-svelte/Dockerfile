FROM node:10.15.2-alpine
RUN mkdir /frontend
WORKDIR /frontend
COPY . /frontend/
RUN npm install
RUN npm run build 