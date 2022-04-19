FROM node:14

WORKDIR /app
COPY server.js /app
COPY package.json /app
RUN npm install

EXPOSE 3000

CMD ["node", "server.js"]
