from .ship import Ship

class ShipDistribution:
    def __init__(self, ship: Ship):
        self.ship = ship
        self.orientation = 0                # Para decir que el barco está sin posicionar
        self.state = "FREE"
        self.places = []

    #DEUDA TÉCNICA: IMPLEMENTAR METODOSx1