FROM python:3-slim-buster
RUN apt-get update && \
apt-get upgrade && \
apt-get install -y \
apt-utils \
build-essential \
git \
gcc \
g++ \
make \
autoconf \
automake \
libtool \
libfreetype6-dev \
libjpeg-dev \
libsdl-dev \
libportmidi-dev \
libsdl-ttf2.0-dev \
libsdl-mixer1.2-dev \
libsdl-image1.2-dev \
python3-rpi.gpio \
python3-pip
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./CODE2000.TTF ./main.py ./
CMD python3 main.py
