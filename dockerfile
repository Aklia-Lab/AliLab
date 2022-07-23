FROM debian

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install nano -y
RUN pip install flask
EXPOSE 5001
WORKDIR /ALILAB