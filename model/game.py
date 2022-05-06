from table import Table

class Game:
    def __init__(self, id: int, player_table_1: Table, player_table_2: Table, num_ship,
                shift: int, hits_player_1: int, hits_player_2: int):
        self.id = id
        self.player_table_1 = player_table_1
        self.player_table_2 = player_table_2
        self.num_ship = num_ship
        self.shift = shift
        self.hits_player_1 = hits_player_1
        self.hits_player_2 = hits_player_2
