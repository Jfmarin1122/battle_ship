from service.list_de_service import ListDEService
from flask import Response, json, jsonify, Blueprint, request
from util.util_encoder import UtilEncoder
from model.ship import Ship

app_list_de = Blueprint("app_list_de", __name__)
list_de_service = ListDEService()

@app_list_de.route('/listde')
def get_all_ships():
    return Response(status=200,
                    response=json.dumps(list_de_service.get_all_ships(),
                                        cls=UtilEncoder), mimetype="application/json")

@app_list_de.route('/listde/add', methods=['POST'])
def add_to_finish():
    data = request.json
    list_de_service.add_to_finish(Ship(data, list_de_service.list_de.count+1))
    return Response(status=200,
                    response=json.dumps({"message": "Barco adicionado exitosamente"}),
                                     mimetype="application/json")

@app_list_de.route('/listde/add_to_start', methods=['POST'])
def add_to_start():
    data = request.json
    list_de_service.add_to_start(Ship(data, list_de_service.list_de.count+1))
    return Response(status=200,
                    response=json.dumps({"message": "Barco adicionado exitosamente"}),
                                     mimetype="application/json")

@app_list_de.route('/create_game')
def create_game():
    return Response(status=200,
                    response=json.dumps(list_de_service.create_game(),
                                        cls=UtilEncoder), mimetype="application/json")

@app_list_de.route('/define_location_ship', methods=['POST'])
def define_location_ship():
    data = request.json
    list_de_service.define_location_ship(data)
    return Response(status=200,
                    response=json.dumps({"message": "Barcos posicionados exitosamente"}),
                    mimetype="application/json")
