class Ship:
    def __init__(self, data, id: int):
        if 'name' in data and 'num_places' in data:
            # En Postman llega un diccionario
            self.name = data['name']
            self.num_places = data['num_places']
            self.id = id
        else:
            raise Exception("Atributos no validos para crear barco")
