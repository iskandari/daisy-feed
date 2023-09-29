# Use the lightweight alpine version of the official Python image
FROM python:3.12-rc-alpine

# Set a directory for the app
WORKDIR /usr/src/app

# Install essential system libraries
RUN apk add --no-cache gcc musl-dev

# Install Python libraries
RUN pip install --no-cache-dir pyais fastapi pyserial uvicorn websockets

# Copy the combined script into the container
COPY norge_ais.py .

# Specify the command to run on container start
CMD ["uvicorn", "norge_ais:app", "--host", "0.0.0.0", "--port", "5000"]
