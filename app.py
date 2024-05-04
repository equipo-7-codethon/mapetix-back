from flask import Flask, request, jsonify
from controllers.event_controller import EventController
from controllers import plan_controller
from controllers import supabase_controller
from auth_middleware import AuthMiddleware

app = Flask(__name__)

event_controller = EventController()
auth_middleware = AuthMiddleware()

  ### GET - /events
@app.route('/events', methods=['GET'])
def get_events():
    jwt_token = request.headers.get('Authorization')

    userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
    ubicacion = request.args.get('userLocation') #obtener la ubicacion del parametro userLocation
    if not ubicacion:
        return jsonify({'error': 'No user location provided'}), 400
    #autenticar toquen y llamar al metodo si es correcto
    if auth_middleware.is_valid_token(userjwt_id):
        plans = plan_controller.get_events(userjwt_id,ubicacion)   
        return jsonify(plans) 
    else:
        return jsonify({'error': 'No authorization token provided'}), 401
    

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
    jwt_token = request.headers.get('Authorization')
    userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
    if auth_middleware.is_valid_token(userjwt_id):
        plans = plan_controller.create_plan(userjwt_id)   
        return jsonify(plans) 
    else:
        return jsonify({'error': 'No authorization token provided'}), 401

 # GET - /plans      Obtiene los planes ya hecho por el usuario (JWT)
@app.route('/plans', methods = ['GET'])
def get_plans_by_user():
    jwt_token = request.headers.get('Authorization')
    userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
    if auth_middleware.is_valid_token(userjwt_id):
        plans = plan_controller.get_plans_by_user(userjwt_id)   
        return jsonify(plans) 
    else:
        return jsonify({'error': 'No authorization token provided'}), 401


if __name__ == '__main__':
    app.run(debug=True)
