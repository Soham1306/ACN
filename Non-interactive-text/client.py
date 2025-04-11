# client_non_interactive_text.py
import socket

HOST = '127.0.0.1'
PORT = 9010
MESSAGE = "This is a non-interactive text message."

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(MESSAGE.encode())
    print("[Client] Message sent.")
