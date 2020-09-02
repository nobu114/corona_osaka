#ベースイメージ
FROM nginx:latest
#設定ファイルのコピー
RUN mkdir -p /etc/nginx
COPY config/nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /etc/letsencrypt
# COPY /etc/letsencrypt/live/raspberrypi-server-nobu.mydns.jp/fullchain.pem /etc/letsencrypt/fullchain.pem
# COPY /etc/letsencrypt/live/raspberrypi-server-nobu.mydns.jp/privkey.pem /etc/letsencrypt/privkey.pem