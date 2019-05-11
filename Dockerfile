FROM ubuntu:latest

LABEL maintainer="Jackuna (github.com/jackuna)"

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN pip3 install django

WORKDIR /usr/local/

RUN git clone https://github.com/Jackuna/djpass.git

WORKDIR /usr/local/djpass/

EXPOSE 9090

CMD ["python3", "manage.py", "runserver", "0.0.0.0:9090"]


