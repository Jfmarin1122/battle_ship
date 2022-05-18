from .user import User
from .list_de import ListDE

class Board:
    def __init__(self, id: int, cols: int, rows: int, player: User, ship_list: ListDE):
        self.id = id
        self.cols = cols
        self.rows = rows
        self.player = player
        self.ship_list = ship_list
        self.board_state = False
        self.received_shoots = []

    def validate_shoot(self, x: int, y: int):
        pass