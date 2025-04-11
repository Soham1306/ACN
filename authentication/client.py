import socket

HOST = '127.0.0.1'
PORT = 9044
username = "soham"
password = "pass123"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(f"{username}:{password}".encode())
    response = s.recv(1024).decode()

    if response == "AUTH_SUCCESS":
        print("[Client] Authenticated. Proceeding...")
    else:
        print("[Client] Authentication failed.")
