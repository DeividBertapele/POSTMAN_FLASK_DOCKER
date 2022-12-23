FROM python:latest

RUN python -m pip install --upgrade pip

WORKDIR /flask_app_postman

ADD . /flask_app_postman/

RUN pip install -r requirements.txt 

CMD [ "python", "main.py" ]