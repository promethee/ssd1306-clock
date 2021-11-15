FROM debian:buster-slim
RUN apt-get update && apt-get install -y build-essential make gcc g++ python3 python3-pip
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip3 install -r ./requirements.txt
COPY ./CODE2000.TTF ./main.py ./
CMD python3 main.py
