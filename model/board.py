from .user import User
from .list_de import ListDE
from .ship_distribution import ShipDistribution
from .coordinate import Coordinate

class Board:
    def __init__(self, id: int, cols: int, rows: int, player: User, ship_list: ListDE):
        self.id = id
        self.cols = cols
        self.rows = rows
        self.player = player
        self.ship_list = ship_list
        self.board_state = False
        self.received_shoots = []

    def validate_shoot_board(self, shoot_x: int, shoot_y: int):
        if shoot_x < self.rows and shoot_y < self.cols:
            for shootsReceived in self.received_shoots:
                if shoot_x == shootsReceived.x and shoot_y == shootsReceived.y:
                    raise Exception("Ya hubo un ataque en la coordenada agregada")
                else:
                    temp = self.ship_list.head
                    while temp is not None:
                        for place in temp.data.places:
                            if place in temp.data.places:
                                ShipDistribution.validate_shoot(place.x, place.y)
                            temp = temp.next
                        return {"message": "Tiro al agua"}
                    self.received_shoots.append(Coordinate(shoot_x, shoot_y, True))
        else:
            raise Exception("Coodernada fuera de dimensiones")

    def add_received_shoots(self, c: Coordinate):
        self.received_shoots.append(c)
