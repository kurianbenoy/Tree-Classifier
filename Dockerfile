# Author: Kurian Benoy
FROM ubuntu:focal

RUN :\
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y  python3.10 \
    && rm -rf /var/lib/apt/lists/*

ENV PATH=/venv/bin:$PATH
RUN python3 -m venv /venv


