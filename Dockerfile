FROM python:3.10.6

WORKDIR /code

RUN pip install --upgrade pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . .

