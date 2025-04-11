import socket
import cv2

HOST = '127.0.0.1'
PORT = 9033

client_socket = socket.socket()
client_socket.connect((HOST, PORT))
cam = cv2.VideoCapture(0)  # Use default webcam

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

try:
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame, encode_param)
        frame_data = buffer.tobytes()
        frame_size = len(frame_data).to_bytes(4, byteorder='big')
        client_socket.sendall(frame_size + frame_data)

        cv2.imshow("Client: Sending Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("[Client] Stopped by user.")
finally:
    cam.release()
    client_socket.close()
    cv2.destroyAllWindows()
