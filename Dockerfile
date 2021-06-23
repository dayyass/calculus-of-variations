FROM python:3.9.5-slim-buster
MAINTAINER Dani El-Ayyass <dayyass@yandex.ru>
WORKDIR /app
COPY . .

# instal dependencies
RUN pip install --no-cache-dir -r requirements.txt

# run bash
CMD bash
