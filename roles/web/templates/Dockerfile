FROM nginx:1.22.0-alpine

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

COPY ./font-end/index.html /usr/share/nginx/html
COPY ./font-end//update.html /usr/share/nginx/html
COPY ./font-end//create.html /usr/share/nginx/html

EXPOSE 81
