FROM node:16.10

COPY . /

WORKDIR /

RUN yarn install

RUN yarn build

CMD ["/bin/sh", "-c", "yarn start"]
