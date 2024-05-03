from flask import Blueprint, render_template

users_bp = Blueprint('users', __name__, url_prefix='/usuarios')

'''
El panel principal de usuarios mostrará recuadros
1. Usuarios (mostrará solo el número de usuarios registrados)
2. Departamento u organización
3. listado de cargos
---

'''

# que la inserción funcione por ajax y que actualice la página
@users_bp.route('/', methods=['GET'])
def panel_principal():
    return render_template('users/users_index.html')

# el agregar usuarios se mostrará como un modal
@users_bp.route('/agregar', methods=['GET','POST'])
def agregar_usuarios():
    return "<><>"

# el editar usuarios se mostrará como un modal

# el panel de usuarios mostrará 