import os
import serial
from fastapi import FastAPI, WebSocket, Depends
from pyais import decode
from pyais.messages import MessageType1, MessageType2, MessageType3, MessageType18
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
PORT = os.getenv("SERIAL_PORT", "/dev/ttyUSB0")


app = FastAPI()

PORT = "YOUR_SERIAL_PORT"  # Replace with the serial port of your dAISy AIS receiver, e.g., "/dev/ttyUSB0" or "COM3".
BAUDRATE = 38400
position_types = [MessageType1, MessageType2, MessageType3, MessageType18]
attributes = ["mmsi", "speed", "lat", "lon", "course", "heading", "status", "turn"]

def ais_data_generator():
    with serial.Serial(PORT, BAUDRATE) as ser:
        while True:
            try:
                line = ser.readline().decode('utf-8').strip()
                decoded_message = decode(line)
                if type(decoded_message) in position_types:
                    data_dict = decoded_message.asdict()
                    yield {attr: data_dict[attr] for attr in attributes if attr in data_dict}
            except Exception as e:
                logger.error(f"Error processing message: {e}")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    for data in ais_data_generator():
        await websocket.send_json(data)
