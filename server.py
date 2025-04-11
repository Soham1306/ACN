# server_interactive.py
import socket

HOST = '127.0.0.1'
PORT = 9002
SAVE_PATH = 'interactive_received_image.jpg'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Waiting for connection...")
    conn, addr = s.accept()
    with conn:
        print(f"[Server] Connected by {addr}")
        
        # Step 1: Receive the image size header
        size_header = conn.recv(16)
        if not size_header:
            print("[Server] No header received.")
            exit()
        image_size = int(size_header.decode().strip())
        print(f"[Server] Expecting image of size: {image_size} bytes")

        # Step 2: Receive image data
        data = b''
        while len(data) < image_size:
            packet = conn.recv(4096)
            if not packet:
                break
            data += packet
            print(f"[Server] Received {len(data)}/{image_size} bytes", end='\r')

        with open(SAVE_PATH, 'wb') as f:
            f.write(data)
        print(f"\n[Server] Image saved as {SAVE_PATH}")

        # Step 3: Send confirmation back
        confirmation = "Image received successfully!"
        conn.sendall(confirmation.encode())
        print("[Server] Confirmation sent to client.")
