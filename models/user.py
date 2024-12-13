from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id: int, email: str, password: str, role: str = "user", triviaId:int = 0):
        self.id = id
        self.email = email
        self.password = password
        self.role = role
        self.triviaId = triviaId
    
    def get_id(self):
        return str(self.id)