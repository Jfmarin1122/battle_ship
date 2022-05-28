from model.list_de import ListDE
from model.ship import Ship
from model.ship_distribution import ShipDistribution
from model.game import Game
from model.user import User
from model.type_user import TypeUser

class ListDEService:
    def __init__(self):
        self.list_de = ListDE()
        self.player1 = User({'email': "jugador1@gmail.com", 'password': '12345'},
                                  2, TypeUser('2', 'Jugador'))
        self.player2 = User({'email': "jugador2@gmail.com", 'password': '12345'},
                                  3, TypeUser('3', 'Jugador'))
        self.game = None

    def get_all_ships(self):
        if self.list_de.head is None:
            return {"message": "La lista esta vacia"}
        else:
            return self.list_de.get_all_ships()

    def add_to_finish(self, data: Ship):
        ship_dist = ShipDistribution(data)
        self.list_de.add_to_finish(ship_dist)
        return {"message": "Barco adicionado exitosamente"}

    def add_to_start(self, data: Ship):
        ship_dist = ShipDistribution(data)
        self.list_de.add_to_start(ship_dist)
        return {"message": "Barco adicionado exitosamente"}

    def clone_list(self):
        return self.list_de.clone_list().get_all_ships()

    def create_game(self):
        self.game = Game(self.player1, self.player2, self.list_de, 1)
        return self.game

    def define_location_ship(self, data):
        pass
