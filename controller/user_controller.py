from flask import request, jsonify, Blueprint
from service.user_service import UserService

app_list_user = Blueprint("app_list_user", __name__)

@app_list_user.route('/list_user/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['TypeUser'] == "Administrador":
        return UserService.token(UserService, data=request.get_json())
    else:
        response = jsonify({"message": "Usuario no valido"})
        response.status_code = 404
        return response

@app_list_user.route('/list_user/verificar_token')
def verify_token():
    token = (request.headers['Authorization'].split(" ")[1])
    return UserService.validate_token(UserService, token, output=True)
