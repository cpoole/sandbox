from ubuntu:18.04

ENV TERM xterm-256color

RUN apt-get update && apt-get install -y \
    git \
    wget \
    unzip \
    ca-certificates \
    build-essential \
    openssl \
    curl \
    vim \
    jq \
    postgresql-client-10 \
    libffi-dev \
    libssl-dev \
    python3 \
    python3-pip \
    redis-tools 


RUN pip3 install --no-cache-dir awscli requests requests-aws4auth boto3

RUN wget -O /tmp/helm.tar.gz https://storage.googleapis.com/kubernetes-helm/helm-v2.11.0-linux-amd64.tar.gz &&\
    cd /tmp && \
    tar xzvf helm.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/helm && \
    chmod +x /usr/local/bin/helm

# Setup Kubectl
RUN apt-get update && apt-get install -y gnupg-agent && \
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list && \
    apt-get update && \
    apt-get install -y kubectl

