FROM node:10

WORKDIR /opt/app/

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true

COPY ./ ./

RUN npm install --registry https://registry.npm.taobao.org  --no-cache && npm run build

FROM nginx:alpine

WORKDIR /opt/dist/

COPY --from=0 /opt/app/dist/* ./

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

COPY ./nginx_proxy.conf /etc/nginx/conf.d/default.conf

CMD ["nginx"]
