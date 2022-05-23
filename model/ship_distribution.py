from .ship import Ship
from .coordinate import Coordinate
# from .board import Board

class ShipDistribution:
    def __init__(self, ship: Ship):
        self.ship = ship
        self.orientation = 0                # Para decir que el barco está sin posicionar
        self.state = "FREE"
        self.places = []

    def validate_coordinate(self, coordinate: Coordinate):
        for coord in self.places:
            if coord.x == coordinate.x and coord.y == coordinate.y:
                return True
        return False

    def add_coordinate(self, x: int, y: int):
        Coord = Coordinate(x, y, True)
        self.places.append(Coord)

    def define_location(self, x: int, y: int, orientation: int):
        if orientation == 0:
            raise Exception("Orientacion no definida")
        elif orientation == 1:
            num_ships_places = self.ship.num_places
            num_validations = x + num_ships_places
            for coordinate in range(x, num_validations + 1):
                new_coordinate = Coordinate(coordinate, y)
                if self.validate_coordinate(new_coordinate):
                    continue
                else:
                    break
        elif orientation == 2:
            num_ships_places = self.ship.num_places
            num_validations = y + num_ships_places
            for coordinate in range(x, num_validations + 1):
                new_coordinate = Coordinate(x, coordinate)
                if self.validate_coordinate(new_coordinate):
                    continue
                else:
                    break

    def validateShoot(self, x:int, y:int):
        count = 0
        num_Ships_Places = self.ship.num_places
        for coordinate in self.places:
            if x == coordinate.x and y == coordinate.y:
                raise Exception("Toco un barco")
                c=Coordinate(x, y,True)
                Table.addReceived_Shoots(c)
            else:
                raise Exception("Toco un agua")
                c=Coordinate(x,y, True)
                Table.addReceived_Shoots(c)
        for x in self.places:
            if x.state == True:
                count += 1
        if count == num_Ships_Places:
            raise Exception("Hundio el barco")
