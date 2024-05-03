from flask import Blueprint, render_template
from app.forms import UserLogin

access_bp = Blueprint('access', __name__)

@access_bp.route('/')
def incio():
    return render_template('access/index.html')

@access_bp.route('/ingresar')
def login():
    form = UserLogin()
    return render_template('access/principal_login.html', form=form)