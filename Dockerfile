FROM python:3.10-slim-bullseye as base 

WORKDIR /src

COPY  django requirements.txt  .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --no-cache-dir -r requirements.txt 

RUN chmod +x manage.py  wait-for-it.sh start-django.sh

USER 1000

WORKDIR /src

CMD [ "./start-django.sh" ]

