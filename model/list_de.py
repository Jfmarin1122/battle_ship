from .node_de import NodeDE
from .ship_distribution import ShipDistribution

class ListDE:
    def __init__(self):
        self.head = None
        self.count = 0

    def get_all_ships(self):
        ships = []
        temp = self.head
        while temp is not None:
            ships.append(temp.data)
            temp = temp.next
        return ships

    def add_to_finish(self, data: ShipDistribution):
        if self.head is None:
            self.head = NodeDE(data)
            self.head.previous = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            new_node = NodeDE(data)
            temp.next = new_node
            new_node.previous = temp
        self.count += 1

    def add_to_start(self, data: ShipDistribution):
        if self.head is None:
            self.head = NodeDE(data)
            self.head.previous = None
        else:
            new_node = NodeDE(data)
            self.head.previous = new_node
            self.head.previous.next = self.head
            self.head = self.head.previous
        self.count += 1

    def validate_coordinate_list_de(self, list_coordinates: []):
        temp = self.head
        while temp is not None:
            try:
                for coordinate in range(len(list_coordinates)):
                    if ShipDistribution.validate_coordinate():
                        list_coordinates.state = True
                temp = temp.next
            except:
                raise Exception({"Coordenadas invalidas para ubicar el barco"})

    def clone_list(self):
        ships = ListDE()
        temp = self.head
        while temp is not None:
            ships.add_to_finish(temp.data)
            temp = temp.next
        return ships
