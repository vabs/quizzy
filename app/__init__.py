from flask import Flask
from flask_socketio import SocketIO
from flask_assets import Environment, Bundle


socketio = SocketIO()
connected_players = {}

from .blueprints.base.base import base as base_blueprint
from .blueprints.score.score import score as score_blueprint


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'quizzy_1312jasd$#asdj!'

    app.register_blueprint(base_blueprint)
    app.register_blueprint(score_blueprint)

    #assets setup
    assets = Environment(app)
    base_js = Bundle('js/jquery.js', 'js/socket.io.min.js', 'js/isotope.min.js', 'js/quizzy.js', output='packed.js')
    base_css = Bundle('css/bootstrap.min.css', 'css/quizzy.css', output='base.css')
    assets.register('base_js', base_js)
    assets.register('base_css', base_css)

    socketio.init_app(app)
    return app

