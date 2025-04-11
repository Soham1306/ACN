import socket
from cryptography.fernet import Fernet

key = 'FZr5OBJ11VJS9wDbvD-7T68f8-8wnXhwSChUeEGrVdg='
cipher = Fernet(key)

HOST = '127.0.0.1'
PORT = 9043
message = "Secret message for secure transmission."

encrypted = cipher.encrypt(message.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(encrypted)
    print("[Client] Sent encrypted data.")
