from model.list_de import ListDE
from model.ship import Ship
from model.ship_distribution import ShipDistribution

class ListDEService:
    def __init__(self):
        self.list_de = ListDE()

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
