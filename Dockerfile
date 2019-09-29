FROM ubuntu:16.04
RUN apt-get -y update
RUN apt-get -y install python3 python3-pip redis-server libpq-dev
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
RUN addgroup --gid 1001 mikhail
RUN useradd mikhail -g mikhail -m -u 1001
USER mikhail