import os
import cv2
from flask import Flask, Response

app = Flask(__name__)

CAMERA_URL = os.getenv("CAMERA_URL")  # IMPORTANT

cap = cv2.VideoCapture(CAMERA_URL)

def generate():
    while True:
        success, frame = cap.read()
        if not success:
            continue

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return "<h1>Camera Stream</h1><img src='/video'>"

@app.route('/video')
def video():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)