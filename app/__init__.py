from flask import Flask
from .routes.access import access_bp
from .routes.users import users_bp

app = Flask(__name__)

# secret_key para el formulario 'aBX_146dF'
app.config["SECRET_KEY"] = 'j2v0t2p4Teching'

app.register_blueprint(access_bp)
app.register_blueprint(users_bp)