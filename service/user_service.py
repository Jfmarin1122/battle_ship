from model.user import TypeUser, User

class UserService:
    def __init__(self):
        self.userList = []
        self.userList.append(User({'email': "felipemarin1109@gmail.com", 'password': '12345'},
                                  1, TypeUser('1', 'Admininistrador')))

    def get_users(self):
        list = []
        for user in self.userList:
            list.append(user.toUserDTO())
        return list

    def validate_user(self, email: str, admin: bool, cant_player: int):
        cont = 0
        for user in self.userList:
            if user.email == email:
                return True
            if admin is False and user.type_user.code == 1:
                return True
            if user.type_user.code == 2:
                cont += 1
        if cant_player == cont:
            return True
        return False

    def create_user(self, data):
        admin = False
        if data['type_user']['code'] == 1:
            admin = True
        if self.validate_user(data['email'], True, 2):
            raise Exception("No cumplen las condiciones para agregar el usuario")

    def login(self, email, password):
        for user in self.userList:
            if email == user.email and password == user.password:
                return user
        return None
