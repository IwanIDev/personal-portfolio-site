FROM nginx:mainline-alpine
WORKDIR /usr/share/nginx/html
COPY output/ . 
COPY nginx.conf /etc/nginx/conf.d/default.conf
