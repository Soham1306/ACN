import socket
import os

HOST = '127.0.0.1'
PORT = 9032
VIDEO_PATH = "file_example_MP4_480_1_5MG.mp4"

if not os.path.exists(VIDEO_PATH):
    print("[Client] File not found.")
    exit()

with open(VIDEO_PATH, 'rb') as f:
    video_data = f.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(f"{len(video_data):<16}".encode())
    s.sendall(video_data)
    print("[Client] Video sent. Waiting for server reply...")

    reply = s.recv(1024).decode()
    print(f"[Client] Server replied: {reply}")
