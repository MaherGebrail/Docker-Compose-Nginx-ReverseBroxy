FROM nginx

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY ./certs/MyCertificate.crt /etc/nginx/certs/
COPY ./certs/MyKey.key /etc/nginx/certs/
