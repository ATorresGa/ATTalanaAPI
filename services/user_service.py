import re
from models.user import User
from typing import List, Optional

users: List [User] = []

def is_valid_password(password:str) -> bool:
    # Validación de la clave: mínimo 8 caracteres, al menos una mayúscula, una minúscula, un número y un carácter especial
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return bool(pattern.match(password))
 
def create_user(email:str, password:str) -> User:
    if len(users)>0:
        if any(user.email == email for user in users):
            raise ValueError("Este correo ya esta en uso")
    
    if not is_valid_password(password):
        raise ValueError('La clave debe de tener al menos 8 caracteres, incluir una mayuscula, un número y un caracter especial')
    
    user_id = len(users)+1
    user = User(user_id,email, password)
    users.append(user)
    return user

def get_users() -> List[User]:
    return users

def find_user(email:str) -> Optional[User]:
    return next ((user for user in users if user.email == email) ,None)

def check_user_credentials (email:str, password:str) -> bool :
    user = find_user(email)
    return user is not None and user.password == password

def edit_user (email:str,role:str, triviaId:int) -> Optional[User]:
    user = find_user(email)
    if user is None:
        raise ValueError("El usuario seleccionado no existe")
    
    updatedUser = User(
            id=user.id,
            password=user.password,
            email=user.email,
            role=role,
            triviaId=triviaId,
    )
    users[user.id - 1] = updatedUser

    editedUser = find_user(email)

    return editedUser

def get_user_by_id (id:int) -> Optional[User]:
    return next((user for user in users if user.id == id), None)
