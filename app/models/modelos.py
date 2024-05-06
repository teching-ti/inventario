from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

# acceso como admin
class UsuarioAccesoSistema(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable = False)
    password_hash = db.Column(db.String(128), nullable=False)
    profile = db.Column(db.String(10))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_passworkd(self, password):
        return check_password_hash(self.password_hash, password)