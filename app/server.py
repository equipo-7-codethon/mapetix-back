from flask import Flask
from app.middleware.errorhandler import ErrorHandler
from app.router import Router

app = Flask(__name__)
Router(app)
ErrorHandler(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)