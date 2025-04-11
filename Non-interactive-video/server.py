import socket

HOST = '127.0.0.1'
PORT = 9031
SAVE_PATH = 'received_video.mp4'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Waiting for video...")

    conn, addr = s.accept()
    with conn:
        print(f"[Server] Connected by {addr}")
        size_header = conn.recv(16)
        file_size = int(size_header.decode().strip())

        data = b''
        while len(data) < file_size:
            packet = conn.recv(4096)
            if not packet:
                break
            data += packet

        with open(SAVE_PATH, 'wb') as f:
            f.write(data)

        print(f"[Server] Video saved as {SAVE_PATH}")
