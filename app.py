from flask import Flask, request
from controllers import EventController
from controllers import PlanController

app = Flask(__name__)

event_controller = EventController()
plan_controller = PlanController()

 ### GET - /events
@app.route('/events', methods=['GET'])
def get_events():
    return event_controller.get_events(request)

### DELETE - /plan/:id    Elimina un plan (id = plan_id)
@app.route('/plan/<int:id>', methods=['DELETE'])
def delete_plan(id):
    return plan_controller.delete_plan(id)

 # GET - /plan/:id   Devuelve un plan concreto de un usuario (id = plan_id)
@app.route('/plan/<int:id>',methods=['GET'])
def get_plan(id):
    return plan_controller.get_plan(id)

### PUT - /plan/:id
@app.route('/plan/<int:id>',methods=['PUT'])
def modify_plan(id):
    plan_data = request.get_json()
    return plan_controller.modify_plan(id,plan_data)

# POST - /plan      Crea un plan para un usario (JWT)
@app.route('/plan', methods = ['POST'])
def create_plan(jwt_token):
    return plan_controller.create_plan(jwt_token)

 # GET - /plans      Obtiene los planes ya hecho por el usuario (JWT)
@app.route('/plans', methods = ['GET'])
def get_plans_by_user(jwt_token):
    return plan_controller.get_plans_by_user(jwt_token)

if __name__ == '__main__':
    app.run(debug=True)
