from service.list_de_service import ListDEService
from flask import Response, json, jsonify, Blueprint, request

app_list_de = Blueprint("app_list_de", __name__)
list_de_service = ListDEService()


