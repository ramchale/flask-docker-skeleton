FROM python:3.6-alpine

WORKDIR /app/src

COPY . /app

RUN apk add --no-cache uwsgi-python3
RUN pip install -r requirements.txt
RUN pip install -r ../tests/requirements.test.txt

CMD [ "uwsgi", "/app/src/uwsgi.ini" ]
