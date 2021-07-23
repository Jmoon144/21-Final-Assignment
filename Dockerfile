FROM python:3
ENV PYTHONUNBUFFERED 0

WORKDIR /usr/src/app

ADD requirements.txt ./

RUN pip install -r requirements.txt
