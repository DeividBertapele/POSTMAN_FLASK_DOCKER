FROM python:latest

RUN python -m pip install --upgrade pip

WORKDIR /flask_app

ADD . /flask_app/

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]