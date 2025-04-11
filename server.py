import socket

USERS = {"soham": "pass123", "admin": "admin123"}

HOST = '127.0.0.1'
PORT = 9044

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Waiting for auth...")

    conn, addr = s.accept()
    with conn:
        creds = conn.recv(1024).decode().split(":")
        username, password = creds

        if USERS.get(username) == password:
            conn.sendall(b"AUTH_SUCCESS")
            print(f"[Server] {username} authenticated.")
        else:
            conn.sendall(b"AUTH_FAILED")
            print("[Server] Authentication failed.")
