FROM node:14-alpine

WORKDIR /turnos-medicos-svelte

COPY rollup.config.js ./
COPY package*.json ./

RUN npm install



COPY ./src ./src
COPY ./public ./public

RUN npm run-script build

ENV HOST=0.0.0.0

EXPOSE 5000

CMD [ "npm", "run", "dev" ]