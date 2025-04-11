# client_interactive.py
import socket
import os

HOST = '127.0.0.1'
PORT = 9002
IMAGE_PATH = "image.jpg"  # Use just the file name if it's in the same folder

# Confirm image exists
if not os.path.exists(IMAGE_PATH):
    print(f"[!] File not found: {os.path.abspath(IMAGE_PATH)}")
    exit()

# Read image
with open(IMAGE_PATH, 'rb') as f:
    img_data = f.read()
image_size = len(img_data)

# Connect to server and send image
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"[Client] Connecting to server at {HOST}:{PORT}...")
    s.connect((HOST, PORT))

    # Send image size as 16-byte header
    s.sendall(f"{image_size:<16}".encode())

    # Send image data
    s.sendall(img_data)
    print("[Client] Image sent. Waiting for server response...")

    # Receive response from server
    response = s.recv(1024).decode()
    print(f"[Client] Server replied: {response}")
