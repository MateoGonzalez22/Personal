FROM node:14

WORKDIR /imagen
COPY app.js /imagen
COPY package.json /imagen
RUN npm install
EXPOSE 3000

CMD ["node", "app.js"]
