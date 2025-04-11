# client_interactive_text.py
import socket

HOST = '127.0.0.1'
PORT = 9011
message = "Hello from the interactive client!"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(message.encode())
    print("[Client] Message sent. Waiting for reply...")

    # Receive reply
    reply = client.recv(1024).decode()
    print(f"[Client] Server replied: {reply}")
