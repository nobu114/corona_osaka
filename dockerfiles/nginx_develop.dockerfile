#ベースイメージ
FROM nginx:latest
#設定ファイルのコピー
RUN mkdir -p /etc/nginx
COPY config/nginx_develop.conf /etc/nginx/nginx.conf