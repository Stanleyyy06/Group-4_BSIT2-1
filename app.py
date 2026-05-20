from flask import Flask, render_template, Response
import os
import cv2

app = Flask(__name__)

# Replace with your IP camera RTSP URL
RTSP_URL = "rtsp://192.168.1.126:10554/tcp/av0_0"

# Open the RTSP stream
camera = cv2.VideoCapture(RTSP_URL)

def generate_frames():
    while True:
        success, frame = camera.read()

        if not success:
            print("Failed to grab frame")
            break
        else:
            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # Stream frame to browser
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route("/")
def home():
    return render_template("camera.html")

@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
