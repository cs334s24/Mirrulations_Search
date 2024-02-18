# builds react app from the source code and runs it in a container.

# Path: react-app/Dockerfile
# Compare this snippet from Dockerfile:
FROM node:16.13.0-alpine3.14

WORKDIR /app

EXPOSE 3000

COPY package.json /app
RUN npm install

COPY . /app

CMD ["npm", "start"]