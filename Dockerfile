FROM python:3-alpine
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre

WORKDIR /source/app
COPY /app source/app
COPY ./requirements.txt /source
COPY ./wsgi.ini /source
COPY ./wsgi.py /source

RUN pip install -r /source/requirements.txt

RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

EXPOSE 3030

CMD ["uwsgi", "--ini", "/source/wsgi.ini"]