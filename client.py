import socket
import hashlib

HOST = '127.0.0.1'
PORT = 9041
data = "This is test data."

# Create checksum
checksum = hashlib.md5(data.encode()).hexdigest()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Send both data and checksum
    s.sendall(f"{checksum}::{data}".encode())
