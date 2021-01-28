import io
import time
from flask import Flask, request, jsonify, send_file

from undistorter import get_transform, undistorter

app = Flask(__name__)

transform_matrix = None
dimensions = None

@app.route('/cornerpin', methods=['POST'])
def set_corner_pins():
    payload = request.get_json(force=True)
    global transform_matrix
    global dimensions
    transform_matrix, dimensions = get_transform(**payload)
    print(transform_matrix, dimensions)
    ret = {
        'x': dimensions[0],
        'y': dimensions[1]
    }
    return jsonify(ret)

@app.route('/frame', methods=['POST'])
def frame_process():
    start = time.time()
    global transform_matrix
    global dimensions
    img = undistorter(request.get_data(), transform_matrix, dimensions)
    b = io.BytesIO(img[1].tobytes())
    print(time.time() - start)
    return send_file(b, 'image/png')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5115)