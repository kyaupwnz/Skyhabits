FROM python:3.10.6

WORKDIR /code

COPY . .


RUN pip3 install -r /code/requirements.txt

