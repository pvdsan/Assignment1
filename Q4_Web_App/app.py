from flask import Flask, render_template, Response, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

# Camera setup
cap = cv2.VideoCapture(1)

# Camera intrinsic parameters
camera_matrix = np.array([[826.1702, 0, 306.2125],
                          [0, 815.7698, 233.2915],
                          [0, 0, 1]])
Z = 30  # Distance to object plane in cm

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/calculate_dimensions', methods=['POST'])
def calculate_dimensions():
    data = request.json
    x_start, y_start, x_end, y_end = data['xStart'], data['yStart'], data['xEnd'], data['yEnd']
    # Calculate dimensions
    width, height = get_dimensions_from_box(x_start, y_start, x_end, y_end, Z, camera_matrix)
    return jsonify({"width": width, "height": height})

@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')

def get_dimensions_from_box(x_start, y_start, x_end, y_end, Z, camera_matrix):
    """Calculates the real-world dimensions from bounding box coordinates."""
    def pixel_to_realworld(u, v, Z, camera_matrix):
        """Converts pixel coordinates to real-world coordinates."""
        inv_camera_matrix = np.linalg.inv(camera_matrix)
        uv1 = np.array([u, v, 1])
        Xc = np.dot(inv_camera_matrix, uv1) * Z
        return Xc[0], Xc[1]
    X_start, Y_start = pixel_to_realworld(x_start, y_start, Z, camera_matrix)
    X_end, Y_end = pixel_to_realworld(x_end, y_end, Z, camera_matrix)
    width = np.abs(X_end - X_start)
    height = np.abs(Y_end - Y_start)
    return width, height

if __name__ == '__main__':
    app.run(debug=True)
