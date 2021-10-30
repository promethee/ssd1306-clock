FROM debian:buster-slim
RUN apt-get update
RUN apt-get install -y build-essential make gcc g++ python3 python3-pip python3-pillow
RUN pip3 install setuptools adafruit-circuitpython-ssd1306 adafruit-blinka RPi.GPIO fonts font-roboto
WORKDIR /usr/src/app
COPY ./main.py ./
CMD python3 main.py
