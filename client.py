import socket
import zlib

HOST = '127.0.0.1'
PORT = 9042
data = "This is some large text or file content." * 50

compressed_data = zlib.compress(data.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(compressed_data)
    print("[Client] Sent compressed data.")
