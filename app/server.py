from flask import Flask
from flask_socketio import SocketIO
from app.middleware.errorhandler import ErrorHandler
from app.router import Router

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

Router(app)
ErrorHandler(app)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)