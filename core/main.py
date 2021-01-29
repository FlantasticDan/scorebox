import time
import base64

from flask import Flask, request, jsonify, send_file
from flask_socketio import SocketIO, emit

from undistorter import get_transform, undistorter

app = Flask(__name__)
socketio = SocketIO(app, logger=True)

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

# @app.route('/frame', methods=['POST'])
# def frame_process():
#     start = time.time()
#     global transform_matrix
#     global dimensions
#     img = undistorter(request.get_data(), transform_matrix, dimensions)
#     b = io.BytesIO(img[1].tobytes())
#     print(time.time() - start)
#     return send_file(b, 'image/png')

@socketio.event
def frame(data):
    print('got frame')
    global transform_matrix
    global dimensions
    img = undistorter(data, transform_matrix, dimensions)
    img_str = str(base64.b64encode(img[1]), 'utf-8')
    payload = f'data:image/png;base64, {img_str}'
    emit('undistort', payload)
    print('finished frame')

if __name__ == '__main__':
    socketio.run(app)