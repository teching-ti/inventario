from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import UsuarioAcceso, UsuarioAccesoRegistro
from app.models.modelos import UsuarioAccesoSistema, db

access_bp = Blueprint('access', __name__)

# ruta de inicio
@access_bp.route('/')
@login_required
def inicio():
    return render_template('access/index.html')

# ruta para acceder al login, en caso de que ya exista una sesion inicada se redirigirá a la ruta de inicio
@access_bp.route('/ingresar', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('access.inicio'))
    
    form = UsuarioAcceso()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = UsuarioAccesoSistema.query.filter_by(username=username).first()
        print(user)
        if user and user.check_password(password):
            login_user(user)
            flash('<i class="fa-regular fa-circle-check fa-xl color-g"></i> Bienvenido al Sistema de Inventario', 'mensaje-ok')
            return redirect(url_for('access.inicio'))
        else:
            # flash message en jinja
            flash('<i class="fa-regular fa-circle-xmark fa-xl color-r"></i> No se pudo iniciar sesión', 'mensaje-error')
    return render_template('access/principal_login.html', form=form)

# ruta para registrar a usuario quer tendría acceso al sistemna 'validar'
@access_bp.route('/registrar_acceso', methods=['GET', 'POST'])
@login_required
def register():
    form = UsuarioAccesoRegistro()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        profile = form.profile.data

        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'mensaje-error')
        else:
            existing_user = UsuarioAccesoSistema.query.filter_by(username = username).first()
            
            if existing_user:
                flash('Error, no se pudo realizar el registro', 'mensaje-error')
            else:
                new_user = UsuarioAccesoSistema(username=username, profile=profile)
                new_user.set_password(password)
                flash('Correcto, registro exitoso', 'mensaje-ok')
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('access.inicio'))
            
    return render_template('access/register_user.html', form=form)

# ruta para salir del sistema
@access_bp.route('/salir')
@login_required
def logout():
    logout_user()
    return redirect(url_for('access.inicio'))