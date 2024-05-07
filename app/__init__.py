from flask import Flask, url_for, redirect
from flask_login import LoginManager
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

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return UsuarioAccesoSistema.query.get(int(user_id))

# Crear las tablas en la base de datos
with app.app_context():
    db.init_app(app)
    db.create_all()
    # instancia de las migraciones
    migrate = Migrate(app, db)

app.register_blueprint(access_bp)
app.register_blueprint(users_bp)

# Manejador para la página no encontrada (404)
@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('access.login'))

# Manejador para la página no encontrada (404)
@app.errorhandler(401)
def page_not_found(error):
    return redirect(url_for('access.login'))