import socket
import os

# ===== CONFIG =====
SERVER_IP = "172.17.114.106"  # <-- Replace with your WSL IP address
PORT = 12345
IMAGE_PATH = "C:/Users/Soham/Downloads/diffOS-client/image.jpg"  # <-- Replace with your actual image path

# ===== LOGIC =====
# Read the image
if not os.path.exists(IMAGE_PATH):
    print(f"[!] File not found: {IMAGE_PATH}")
    exit()

with open(IMAGE_PATH, "rb") as f:
    image_data = f.read()

image_size = len(image_data)

# Connect to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"[+] Connecting to {SERVER_IP}:{PORT}...")
    s.connect((SERVER_IP, PORT))

    print(f"[+] Sending image of size {image_size} bytes...")
    
    # Send image size first (16-byte header, padded)
    s.sendall(f"{image_size:<16}".encode())

    # Send image data
    s.sendall(image_data)

    print("[+] Image sent successfully.")
