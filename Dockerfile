FROM python:3.8.5-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./video_app /app

WORKDIR /app
EXPOSE 80
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]