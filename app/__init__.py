from flask import Flask
from .routes.access import access_bp
from .routes.users import users_bp

from flask_migrate import Migrate
from .models.modelos import db, UsuarioAccesoSistema

app = Flask(__name__)

#Configuración para MySQL en servidor local
#dentro del bloc de notas con las anotaciones de pythonanywhere
#se encuentran las anotaciones de como funcionaría en producción
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://ti:jvteching9830@localhost/inventario_ti"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# secret_key para el formulario 'aBX_146dF'
app.config["SECRET_KEY"] = 'j2v0t2p4Teching'

# Crear las tablas en la base de datos
with app.app_context():
    db.init_app(app)
    db.create_all()
    # instancia de las migraciones
    migrate = Migrate(app, db)

app.register_blueprint(access_bp)
app.register_blueprint(users_bp)