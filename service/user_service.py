from os import getenv
from flask import jsonify
from jwt import encode, decode, exceptions
import time

class UserService:
    def token(self, data):
        expire_token = int(time.time())
        token = encode(payload={**data, "duration": expire_token},
                       key=getenv("secret"), algorithm="HS256")
        return token.encode("UTF-8")

    def validate_token(self, token, output=False):
        try:
            if output is True:
                return decode(token, key=getenv("secret"), algorithms=["HS256"])
            decode(token, key=getenv("secret"), algorithms=["HS256"])
        except exceptions.DecodeError:
            response = jsonify({"message": "Token Invalido"}, status=401)
            return response
        except exceptions.ExpiredSignatureError:
            response = jsonify({"message": "Token expirado"}, status=401)
            return response

