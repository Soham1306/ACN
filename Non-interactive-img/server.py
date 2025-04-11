# server_non_interactive.py
import socket

HOST = '127.0.0.1'
PORT = 9001
SAVE_PATH = 'non_interactive_image.jpg'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Waiting for connection...")
    conn, addr = s.accept()
    with conn:
        print(f"[Server] Connected by {addr}")
        # Receive a fixed-length header (16 bytes) that indicates the image size.
        size_header = conn.recv(16)
        total_size = int(size_header.decode().strip())
        data = b''
        # Receive the image data until the total size is reached.
        while len(data) < total_size:
            packet = conn.recv(4096)
            if not packet:
                break
            data += packet
        # Save the received image to disk.
        with open(SAVE_PATH, 'wb') as f:
            f.write(data)
        print(f"[Server] Image saved as {SAVE_PATH}")
