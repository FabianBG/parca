FROM python:3.6-alpine

WORKDIR /parca

COPY ./* /parca/

VOLUME [ "/models", "/tmp" ]

ENTRYPOINT [ "sh" ]