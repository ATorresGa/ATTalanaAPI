#agregar actividad al usuario para cuando se borre su cuenta dejarlo como inactivo
from flask import Flask, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from controllers.user_controller import user_blueprint
from controllers.trivia_controller import trivia_blueprint
from controllers.participation_controller import participation_blueprint
from controllers.ranking_controller import ranking_blueprint

app = Flask(__name__)
app.secret_key = "secret_key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message="Debes de inicar sesión para acceder a éste recurso"

app.register_blueprint(user_blueprint, url_prefix="/talatrivia")
app.register_blueprint(trivia_blueprint, url_prefix="/talatrivia")
app.register_blueprint(participation_blueprint, url_prefix="/talatrivia")
app.register_blueprint(ranking_blueprint, url_prefix="/talatrivia")

@app.route("/")
def welcome ():
    return jsonify({"message": "Bienvenido a TalaTrivia"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
