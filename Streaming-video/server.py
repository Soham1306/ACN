import socket
import cv2
import numpy as np

HOST = '127.0.0.1'
PORT = 9033

server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("[Server] Waiting for video stream...")

conn, addr = server_socket.accept()
print(f"[Server] Connected by {addr}")

data = b""
payload_size = 4  # sending length of each frame

while True:
    # Receive frame size
    while len(data) < payload_size:
        packet = conn.recv(4096)
        if not packet:
            break
        data += packet

    if len(data) < payload_size:
        break

    frame_size = int.from_bytes(data[:payload_size], byteorder='big')
    data = data[payload_size:]

    # Receive the actual frame
    while len(data) < frame_size:
        data += conn.recv(4096)

    frame_data = data[:frame_size]
    data = data[frame_size:]

    frame = cv2.imdecode(np.frombuffer(frame_data, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow("Server: Receiving Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

conn.close()
cv2.destroyAllWindows()
