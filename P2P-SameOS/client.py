# image_sender.py
import socket

HOST = 'localhost'
PORT = 5001
FILENAME = 'image.jpg'  # Change to any image you want to send

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("[Client] Connected to server")

with open(FILENAME, 'rb') as f:
    data = f.read()
    client.sendall(data)

print("[Client] Image sent")
client.close()
