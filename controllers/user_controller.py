from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from flask_login import login_user, logout_user, login_required, current_user
from schemas.user_schemas import UserCreateSchema, UserResponseSchema, UserEditSchema, UserEditResponseSchema
from schemas.login_schema import LoginSchema
from services.user_service import create_user, get_users, check_user_credentials, find_user, edit_user

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route ("/create-user/", methods = ["POST"])
def create_user_ep():
    try:
        data = request.get_json()
        userSchema = UserCreateSchema(**data)
        createdUser = create_user(userSchema.email, userSchema.password)
        return jsonify(UserResponseSchema(email = createdUser.email, id= createdUser.id).model_dump()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@user_blueprint.route("/login/", methods = ["POST"])
def login_ep():
    # agregar validacion para no hacer doble login
    try:
        data = request.get_json()
        loginSchema = LoginSchema(**data)

        email = loginSchema.email
        password = loginSchema.password
    except ValidationError as e:
        return jsonify({"error":str(e)}), 400
    
    user = find_user(email)
    if user == None:
        return jsonify({"message":"No existe una cuenta con ese email"})
    if not user or not check_user_credentials(email, password):
        return jsonify({"message": "Credenciales invalidas"}), 401
    # if user.is_authenticated:
    #     return jsonify({"message":"Ya tienes una sesión iniciada, cierra sesión antes de inicar otra"})
    if check_user_credentials(loginSchema.email, loginSchema.id):
        login_user(user)
        return jsonify({"message": "Login éxitoso"}), 200
    return jsonify({"error":"Credenciales no validas"}), 401

@user_blueprint.route("/get-users/", methods=["GET"])
# @login_required
def get_users_ep():
    users = get_users()
    return jsonify([UserResponseSchema(email=user.email, id=user.id).model_dump() for user in users]), 200

@user_blueprint.route("/logout/", methods=["POST"])
# @login_required
def logout_ep():
    try:
        if not current_user.is_authenticated:
            return jsonify({"message": "No estás autenticado"}), 400
        logout_user()
        return jsonify({"message": "Logout exitoso"}), 200
    except ValueError as e:
                return jsonify({"error":str(e)}), 400
                

@user_blueprint.route("/edit-user/", methods=["POST"])
def edit_user_ep():
     try:
          data = request.get_json()
          userEditSchema = UserEditSchema(**data)
          editedUser = edit_user(email=userEditSchema.email, role=userEditSchema.role, triviaId= userEditSchema.triviaId)
          return jsonify(UserEditResponseSchema(id=editedUser.id, email=editedUser.email, role=editedUser.role, triviaId=editedUser.triviaId).model_dump()), 202
     except ValueError as e:
          return jsonify({"error":str(e)}), 400    