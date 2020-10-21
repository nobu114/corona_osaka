# debian busterベースのpythonイメージを使用 ver3.8.5
FROM python:3.8.5-buster

RUN echo 'deb http://download.opensuse.org/repositories/shells:/fish:/release:/3/Debian_10/ /' | tee /etc/apt/sources.list.d/shells:fish:release:3.list
RUN curl -fsSL https://download.opensuse.org/repositories/shells:fish:release:3/Debian_10/Release.key | gpg --dearmor | tee /etc/apt/trusted.gpg.d/shells:fish:release:3.gpg > /dev/null
RUN apt-get update
RUN apt-get install -y fish
RUN curl -fsSL https://code-server.dev/install.sh | sh -s -- --dry-run
RUN curl -fsSL https://code-server.dev/install.sh | sh
RUN code-server


