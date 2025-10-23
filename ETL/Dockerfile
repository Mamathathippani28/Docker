FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Ass1.py .
COPY customers-100.csv .
#COPY docker-compose.yaml

EXPOSE 8000

CMD [ "python", "Ass1.py" ]


