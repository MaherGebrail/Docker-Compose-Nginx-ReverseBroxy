FROM ubuntu

RUN apt update -y && apt install python3 python3-pip -y && pip3 install flask 

VOLUME ./flask/ /opt/Flask-app/
CMD python3 /opt/Flask-app/app.py 
