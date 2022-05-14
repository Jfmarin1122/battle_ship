from model.ship import Ship
from model.list_de import ListDE

class ListDEService:
    def __init__(self):
        self.ships = ListDE()

    def get_all_ships(self):
        if self.ships.head is None:
            return {"message": "La lista esta vacia"}
        else:
            return self.ships.get_all_ships()

    def add_ship(self, data):
        ship = Ship(data)
        if self.ships.head is None:
            return {"message": "La lista esta vacia"}
        else:
            self.ships.add_to_finish(ship)

    def add_ship_to_start(self, data):
        ship = Ship(data)
        if self.ships.head is None:
            return {"message": "La lista esta vacia"}
        else:
            self.ships.add_to_start(ship)

    def count(self):
        if self.ships.head is None:
            return {"message": "La lista esta vacia"}
        return {"la cantidad de barcos es": self.ships.count()}

    def clonar(self):
        pass
