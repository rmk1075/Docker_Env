FROM ubuntu:18.04

LABEL author="jamie <rmk1075@gmail.com>"

RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev build-essential

WORKDIR /home/app/

COPY test_v01/ .
RUN pip3 install --no-cache-dir -r requirements.txt
