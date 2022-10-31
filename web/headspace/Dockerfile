FROM node:16-slim

WORKDIR /usr/src/app
COPY . .

RUN npm install --production

EXPOSE 8080

CMD ["node", "headspace.js"]

