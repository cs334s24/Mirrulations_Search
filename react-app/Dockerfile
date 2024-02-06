# builds react app from the source code and runs it in a container.

# Path: react-app/Dockerfile
# Compare this snippet from Dockerfile:
FROM node:16.13.0-alpine3.14

WORKDIR /app

COPY package.json .
COPY package-lock.json .
COPY react-app/ .

RUN npm install

COPY . .

CMD ["npm", "start"]