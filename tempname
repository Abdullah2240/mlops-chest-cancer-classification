FROM python:3.10.19-slim-bullseye


RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirments.txt

CMD [ "python", "app.py" ]
