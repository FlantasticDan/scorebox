from flask import Blueprint, render_template, request

import constant
from constant import VERSION
from images import Logos

from main import socketio

LOGOS = Logos()

team = Blueprint('team', __name__, template_folder='templates', static_folder='static')

@team.get('/icon.svg')
def get_icon():
    return team.send_static_file(f'img/{constant.sport}_icon.svg')

@team.get('/setup')
def setup():
    return render_template('setup.html', version=VERSION, sport=constant.displayable_sport())

@team.route('/init', methods=['POST'])
def initialize():
    global LOGOS
    setup = request.form
    files = request.files
    LOGOS.set_home(files['home_logo'].read(), files['home_logo'].filename)
    LOGOS.set_visitor(files['visitor_logo'].read(), files['visitor_logo'].filename)
    return 'OK'
