import socket
import pyaudio

CHUNK = 1024
PORT = 9023
HOST = '127.0.0.1'

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, frames_per_buffer=CHUNK)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[Server] Listening for stream...")

    conn, addr = s.accept()
    with conn:
        print(f"[Server] Streaming from {addr}")
        while True:
            data = conn.recv(CHUNK)
            if not data:
                break
            stream.write(data)

stream.stop_stream()
stream.close()
p.terminate()
