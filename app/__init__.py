from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret!'

    from .views import main as main_bluefrint
    app.register_blueprint(main_bluefrint)

    socketio.init_app(app)
    return app
