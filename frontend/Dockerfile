# builds react app from the source code and runs it in a container.

# Path: react-app/Dockerfile
# Compare this snippet from Dockerfile:
FROM node

WORKDIR /app

EXPOSE 3000

COPY package-lock.json /app
RUN yarn install --frozen-lockfile

COPY . /app

CMD ["npm", "start"]