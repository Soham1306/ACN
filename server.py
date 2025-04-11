import socket
import os

# Server configuration
HOST = '0.0.0.0'      # Listen on all available interfaces
PORT = 12345
OUTPUT_FILE = 'received_image.jpg'

def receive_image(conn):
    # Step 1: Receive fixed-length header with image size
    header = conn.recv(16)
    if not header:
        print("[!] No header received.")
        return False

    img_size = int(header.decode().strip())
    print(f"[+] Expecting image of size: {img_size} bytes")

    # Step 2: Receive image data in chunks
    received_data = b''
    while len(received_data) < img_size:
        chunk = conn.recv(4096)
        if not chunk:
            break
        received_data += chunk
        print(f"[.] Received {len(received_data)}/{img_size} bytes", end='\r')

    # Step 3: Save image
    with open(OUTPUT_FILE, 'wb') as f:
        f.write(received_data)

    print(f"\n[+] Image saved as {OUTPUT_FILE}")
    return True

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[+] Server listening on {HOST}:{PORT}...")

        conn, addr = s.accept()
        with conn:
            print(f"[+] Connection from {addr}")
            if receive_image(conn):
                print("[+] Transfer complete.")
            else:
                print("[!] Transfer failed.")

if __name__ == "__main__":
    start_server()
