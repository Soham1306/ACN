import socket
import hashlib

HOST = '127.0.0.1'
PORT = 9041

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Waiting for data...")

    conn, addr = s.accept()
    with conn:
        raw = conn.recv(1024).decode()
        recv_checksum, recv_data = raw.split("::")
        calculated = hashlib.md5(recv_data.encode()).hexdigest()

        if recv_checksum == calculated:
            print("[Server] Checksum valid. Data:", recv_data)
        else:
            print("[Server] Data corrupted.")
