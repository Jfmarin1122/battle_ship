from .ship import Ship
from .coordinate import Coordinate

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

    def define_location_ship(self, x: int, y: int, orientation: int):
        if orientation == 0:
            raise Exception("Orientacion no definida")
        elif orientation == 1:
            num_ships_places = self.ship.num_places
            num_validations = x + num_ships_places
            for coordinate_y in range(y, num_validations):
                new_coordinate = Coordinate(coordinate_y, y, False)
                if self.validate_coordinate(new_coordinate) is False:
                    self.places.append(new_coordinate)
                    continue
                else:
                    raise Exception({"message": "La coordenada no es valida"})
            self.state = "POSITIONED"
        elif orientation == 2:
            num_ships_places = self.ship.num_places
            num_validations = y + num_ships_places
            for coordinate in range(x, num_validations):
                new_coordinate = Coordinate(x, coordinate, False)
                if self.validate_coordinate(new_coordinate) is False:
                    self.places.append(new_coordinate)
                    continue
                else:
                    raise Exception({"message": "La coordenada no es valida"})
            self.state = "POSITIONED"

    def validate_shoot(self, shoot_x: int, shoot_y: int):
        count = 0
        num_ships_places = self.ship.num_places
        for coordinate in self.places:
            if shoot_x == coordinate.x and shoot_y == coordinate.y:
                coordinate.state = True
                return {"message": "Toco un barco"}
            else:
                return {"message": "Tiro al agua"}
        for x in self.places:
            if x.state is True:
                count += 1
        if count == num_ships_places:
            return {"message": "Barco hundido"}
