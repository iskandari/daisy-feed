import serial
from pyais import NMEAMessage, exceptions, decode
#from pymongo import MongoClient
from pyais.messages import MessageType1, MessageType2, MessageType3, MessageType18

def ais_listener(port, baudrate=38400):
    # Connect to MongoDB
    #client = MongoClient('localhost', 27017)
    #db = client.aisdb
    #collection = db.messages

    with serial.Serial(port, baudrate) as ser:
        while True:
            line = ser.readline().decode('utf-8').strip()
            print(f"Encoded: {line}")

            try:
                decoded = decode(line)

                # Check if the decoded message is one of the desired types
                if isinstance(decoded, (MessageType1, MessageType2, MessageType3,  MessageType18)):
                    print("Decoded:", decoded)

                    # Save decoded data as a dictionary in MongoDB
                    ais_dict = decoded.asdict()
                    collection.insert_one(ais_dict)

            except exceptions.UnknownMessageException as e:
                print(f"Unknown message: {str(e)}")
            except AttributeError as ae:
                print(f"Attribute error occurred: {str(ae)}")

if __name__ == "__main__":
    port = "/dev/tty.usbmodem101"
    baudrate = 38400
    ais_listener(port, baudrate)
