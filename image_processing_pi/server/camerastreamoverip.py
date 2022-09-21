# Import necessary libraries
from flask import Flask, render_template, Response
import cv2
from router import Router
from frames import gen_frames
from flask_cors import CORS
# Initialize the Flask app
app = Flask(__name__, template_folder='template')

app.register_blueprint(Router)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
