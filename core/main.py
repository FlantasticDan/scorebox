from flask import Flask, request

from undistorter import get_transform

app = Flask(__name__)

@app.route('/cornerpin', methods=['POST'])
def set_corner_pins():
    print(request.get_json(force=True))
    return 'OK'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5115)