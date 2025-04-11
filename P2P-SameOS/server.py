# image_receiver.py
import socket

print("[Debug] Server script started")

HOST = 'localhost'
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("[Server] Waiting for connection...")

conn, addr = server.accept()
print(f"[Server] Connected by {addr}")

with open("received_image.jpg", "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("[Server] Image received and saved as 'received_image.jpg'")
conn.close()
