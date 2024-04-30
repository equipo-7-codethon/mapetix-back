from flask import Flask, request
from app.controllers import EventController

app = Flask(__name__)

event_controller = EventController()

@app.route('/events', methods=['GET'])
def get_events():
    return event_controller.get_events(request)

if __name__ == '__main__':
    app.run(debug=True)
