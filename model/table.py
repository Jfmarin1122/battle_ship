from user import User
from list_de import ListDE

class Table:
    def __init__(self, id: int, cols: int, rows: int, player: User, list_ship: ListDE,
                 state_table: bool):
        self.id = id
        self. cols = cols
        self.rows = rows
        self.player = player
        self.list_ship = list_ship
        self.state_table = state_table
