from flask import json, Response, request, jsonify, Blueprint
from util.util_encoder import UtilEncoder
from service.user_service import UserService
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

app_user = Blueprint("app_user", __name__)
user_service = UserService()

@app_user.route('/user')
@jwt_required()
def get_users():
    return Response(status=200,
                    response=json.dumps(user_service.get_users(),
                                        cls=UtilEncoder), mimetype="application/json")

@app_user.route('/list_user/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        user = user_service.login(email, password)
        access_token = create_access_token(identity={'username': user})
        return jsonify({'token': access_token})
    except Exception as e:
        return jsonify({'message': str(e)})
