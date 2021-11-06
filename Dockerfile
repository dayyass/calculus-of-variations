FROM python:3.7-slim-buster
MAINTAINER Dani El-Ayyass <dayyass@yandex.ru>

WORKDIR /workdir
COPY . .

# instal dependencies
RUN pip install --no-cache-dir -r requirements.txt

# run bash
CMD bash
