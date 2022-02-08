from flask_socketio import emit
from app import socketio


@socketio.on('connect')
def connect(auth):
    print("in connect.")
    emit("my response", {"data": "hello"})


@socketio.on('my event')
def test(data):
    print(data)
