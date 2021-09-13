from flask import Flask, render_template, redirect
from flask_socketio import SocketIO, emit

from bundle import bundle
import constant
from constant import VERSION

from team import team

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet', logger=False, engineio_logger=False)

@app.get('/startup')
def startup():
    return render_template('startup.html', version=VERSION)

@app.get('/startup/<sport>')
def startup_sport(sport):
    constant.sport = sport
    app.register_blueprint(team)
    return redirect('/setup')

if __name__ == '__main__':
    constant.init()
    bundle(app)
    socketio.run(app, port=5000)