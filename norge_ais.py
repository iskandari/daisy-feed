from fastapi import FastAPI, WebSocket
from pyais.stream import TCPConnection
from pyais.messages import MessageType1, MessageType2, MessageType3, MessageType18

app = FastAPI()

host = '153.44.253.27'
port = 5631
position_types = [MessageType1, MessageType2, MessageType3, MessageType18]
attributes = ["mmsi", "speed", "lat", "lon", "course", "heading", "status", "turn"]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    for msg in TCPConnection(host, port=port):
        try:
            decoded_message = msg.decode()
            if type(decoded_message) in position_types:
                data_dict = decoded_message.asdict()
                filtered_data = {attr: data_dict[attr] for attr in attributes if attr in data_dict}
                await websocket.send_json(filtered_data)
        except Exception as e:
            print(f"Error processing message: {e}")
            await websocket.close()
            break

