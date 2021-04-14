#ベースイメージ
FROM nginx:latest
#設定ファイルのコピー
RUN mkdir -p /etc/nginx
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /etc/letsencrypt
COPY /etc/letsencrypt /etc/letsencrypt
