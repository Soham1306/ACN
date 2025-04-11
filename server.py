# server_non_interactive_text.py
import socket

HOST = '127.0.0.1'
PORT = 9010
SAVE_FILE = 'message.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Waiting for text message...")

    conn, addr = s.accept()
    with conn:
        print(f"[Server] Connected by {addr}")
        message = conn.recv(1024).decode()
        with open(SAVE_FILE, 'w') as f:
            f.write(message)
        print(f"[Server] Message saved: {message}")
