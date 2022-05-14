from .node_de import NodeDE
from .ship import Ship

class ListDE:
    def __init__(self):
        self.head = None
        self.count = 0

    def count(self):
        count = 0
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            count += 1
        count += 1
        return count

    def get_all_ships(self):
        ships = []
        temp = self.head
        while temp.next is not None:
            ships.append(temp.data)
            temp = temp.next
        ships.append(temp.data)
        return ships

    def validate_coordinate(self, coordinate_x: int, coordinate_y: int):
        temp = self.head
        while temp is not None:
            if temp.data.coordinate.x == coordinate_x and temp.data.coordinate.y == coordinate_y:
                return True
            temp = temp.next
        return False

    def add_to_finish(self, data: Ship):
        if self.validate_coordinate(data.coordinate):
            raise Exception("La coordenada seleccionada ya esta ocupada")
        node = NodeDE(data)
        if self.head is None:
            self.head = node
            self.head.prev = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp

    def add_to_start(self, data: Ship):
        node = NodeDE(data)
        if self.head is None:
            self.head = node
            self.head.prev = None
        else:
            if self.validate_coordinate(data.coordinate):
                raise Exception("La coordenada seleccionada ya esta ocupada")
            node.next = self.head
            self.head.prev = node
            self.head = node

    def clonar(self):
        pass

