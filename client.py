import socket
import pyaudio

CHUNK = 1024
PORT = 9023
HOST = '127.0.0.1'

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNK)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[Client] Streaming audio...")
    try:
        while True:
            data = stream.read(CHUNK)
            s.sendall(data)
    except KeyboardInterrupt:
        print("\n[Client] Stopped streaming.")

stream.stop_stream()
stream.close()
p.terminate()
