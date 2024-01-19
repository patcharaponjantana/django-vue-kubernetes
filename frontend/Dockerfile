FROM node:18.18-alpine

WORKDIR /code

ADD . /code


# BUILD and Run
RUN yarn install & yarn global add serve
RUN yarn build

EXPOSE 3000
CMD ["serve", "-s", "dist"] 