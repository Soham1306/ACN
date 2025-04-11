# client_non_interactive.py
import socket
import os

HOST = '127.0.0.1'
PORT = 9001
# Update this path to point to an actual image file on your system.
IMAGE_PATH = r"image.jpg"  # e.g., r"C:\Users\Soham\Pictures\sample.jpg"

# Check if the image file exists.
if not os.path.exists(IMAGE_PATH):
    print(f"[!] File not found: {IMAGE_PATH}")
    exit()

# Read the image as binary data.
with open(IMAGE_PATH, 'rb') as f:
    img = f.read()

# Create a socket connection to the server.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Create a header with the image size, padded to 16 bytes.
    header = f"{len(img):<16}".encode()
    # Send header concatenated with image data.
    s.sendall(header + img)
    print("[Client] Image sent (non-interactive).")
