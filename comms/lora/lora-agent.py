import serial
import json

ser = serial.Serial('/dev/ttyUSB0', 9600)

def send(data):
    msg = json.dumps(data)
    ser.write(msg.encode())

def receive():
    if ser.in_waiting:
        data = ser.readline().decode()
        return json.loads(data)

if __name__ == "__main__":
    while True:
        data = receive()
        if data:
            print("[LoRa RX]", data)