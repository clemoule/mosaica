FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
  wget \
  unzip \
  openjdk-17-jdk \
  libgtk-3-0 \
  libxtst6 \
  libxrender1 \
  libxext6 \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/gama

# (option) copie GAMA installé localement ou téléchargé
COPY . /workspace