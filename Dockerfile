FROM python:3.10-slim

RUN apt update -y && \
    apt install -y --no-install-recommends \
        awscli \
        build-essential \
        libffi-dev \
        libssl-dev \
        python3-dev \
        libjpeg-dev \
        zlib1g-dev \
        gcc \
    && rm -rf /var/lib/apt/lists/*

RUN apt update -y && apt install awscli -y

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]
