from flask import Flask
from flask_socketio import SocketIO

from .blueprints.base.base import base as base_blueprint

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'quizzy_1312jasd$#asdj!'

    app.register_blueprint(base_blueprint)

    socketio.init_app(app)
    return app

