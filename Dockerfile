FROM debian:buster-slim
RUN apt-get update
RUN apt-get install -y build-essential make gcc g++ python3 python3-pip python3-pillow
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip3 install -r ./requirements.txt
COPY ./main.py ./
CMD python3 main.py
