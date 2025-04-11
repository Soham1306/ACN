import socket
import os

HOST = '127.0.0.1'
PORT = 9022
AUDIO_PATH = "file_example_WAV_1MG.wav"

if not os.path.exists(AUDIO_PATH):
    print("[Client] File not found.")
    exit()

with open(AUDIO_PATH, 'rb') as f:
    audio_data = f.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(f"{len(audio_data):<16}".encode())
    s.sendall(audio_data)
    print("[Client] Audio sent. Waiting for response...")

    reply = s.recv(1024).decode()
    print(f"[Client] Server replied: {reply}")
