from flask import Flask, Response
import cv2

app = Flask(__name__)

CAMERA_URL = "rtsp://admin:888888@192.168.1.126:10554/tcp/av0_0"

cap = cv2.VideoCapture(CAMERA_URL)

def generate_frames():
    while True:
        success, frame = cap.read()

        if not success:
            print("Failed to read camera")
            break

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               frame + b'\r\n')

@app.route('/')
def home():
    return '''
    <h1>IP Camera Stream</h1>
    <img src="/video">
    '''

@app.route('/video')
def video():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
