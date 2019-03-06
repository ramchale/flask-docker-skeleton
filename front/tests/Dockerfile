FROM python:3.6-alpine

WORKDIR /app

COPY ./app /app

RUN apk add --no-cache uwsgi-python3
RUN pip install -r requirements.txt

#CMD [ "uwsgi", "--yaml", "uwsgi.config.yaml:app"]
CMD [ "uwsgi", "--socket", "0.0.0.0:3031", "--uid", "uwsgi", "--plugins", "python3", "--protocol", "uwsgi", "--wsgi", "app:app", "--pythonpath", "/usr/local/lib/python3.6/site-packages" ]
