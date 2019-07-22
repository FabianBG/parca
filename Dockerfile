FROM alpine:3.7

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools

RUN apk add --no-cache jpeg-dev zlib-dev uwsgi-python3

WORKDIR /parca

COPY . /parca/

VOLUME [ "/parca/tmp" ]

RUN pip3 install -r requirements.txt

ENTRYPOINT uwsgi --ini uwsgi.ini