import socket
from cryptography.fernet import Fernet

key = 'FZr5OBJ11VJS9wDbvD-7T68f8-8wnXhwSChUeEGrVdg='
cipher = Fernet(key)

HOST = '127.0.0.1'
PORT = 9043

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Awaiting encrypted data...")

    conn, addr = s.accept()
    with conn:
        encrypted = conn.recv(1024)
        decrypted = cipher.decrypt(encrypted).decode()
        print("[Server] Decrypted message:", decrypted)
