FROM ubuntu

RUN apt update -y && apt install python3 python3-pip -y && pip3 install flask 


