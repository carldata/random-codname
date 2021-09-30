FROM python:3.8-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY random-codname.py .
COPY uwsgi.ini .
COPY start.sh .
COPY nginx.conf /etc/nginx


EXPOSE 8089
RUN chmod +x ./start.sh
CMD ["./start.sh"]
