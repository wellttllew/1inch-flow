FROM ubuntu:18.04 

ADD . /app/1inch-flow

RUN  apt-get update && \
    apt-get install -y python3 python3-pip python3-dev libgraph-easy-perl

RUN cd /app/1inch-flow && \
    pip3 install -r requirements.txt  

WORKDIR /app/1inch-flow 

ENTRYPOINT ["python3","main.py"]