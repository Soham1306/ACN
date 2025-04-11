import socket
import zlib

HOST = '127.0.0.1'
PORT = 9042

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Listening...")

    conn, addr = s.accept()
    with conn:
        compressed = conn.recv(4096)
        data = zlib.decompress(compressed).decode()
        print("[Server] Received and decompressed data:")
        print(data)
