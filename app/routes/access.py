from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.forms import UsuarioAcceso, UsuarioAccesoRegistro, ValidationError
from app.models.modelos import UsuarioAccesoSistema, db

access_bp = Blueprint('access', __name__)

@access_bp.route('/')
def inicio():
    return render_template('access/index.html')

@access_bp.route('/ingresar')
def login():
    form = UsuarioAcceso()
    return render_template('access/principal_login.html', form=form)

@access_bp.route('/registrar_acceso', methods=['GET', 'POST'])
def register():
    form = UsuarioAccesoRegistro()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'mensaje-error')
        else:
            existing_user = UsuarioAccesoSistema.query.filter_by(username = username).first()
            
            if existing_user:
                flash('Error, no se pudo realizar el registro', 'mensaje-error')
            else:
                new_user = UsuarioAccesoSistema(username=username)
                new_user.set_password(password)
                flash('Correcto, registro exitoso', 'mensaje-ok')
                # db.session.add(new_user)
                # db.session.commit()
                return redirect(url_for('access.inicio'))
        
    return render_template('access/register_user.html', form=form)

@access_bp.route('/salir')
def logout():
    logout_user()
    return redirect(url_for('access.inicio'))