# server_interactive_text.py
import socket

HOST = '127.0.0.1'
PORT = 9011

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Waiting for message...")

    conn, addr = s.accept()
    with conn:
        print(f"[Server] Connected by {addr}")
        message = conn.recv(1024).decode()
        print(f"[Server] Received: {message}")

        # Send back acknowledgment
        response = f"Message received: \"{message}\""
        conn.sendall(response.encode())
        print("[Server] Acknowledgment sent.")
