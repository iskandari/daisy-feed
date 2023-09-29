# Use the lightweight alpine version of the official Python image
FROM python:3.12-rc-alpine

WORKDIR /usr/src/app

RUN apk add --no-cache gcc musl-dev
RUN pip install --no-cache-dir pyais fastapi pyserial uvicorn websockets

COPY norge_ais.py .
COPY ais_microservice.py .

CMD ["uvicorn", "norge_ais:app", "--host", "0.0.0.0", "--port", "5000"]
