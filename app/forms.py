from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo

#formulario para el login de usuarios
class UsuarioAcceso(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

# formulario para registrar al usuario que tendrá acceso al sistema
class UsuarioAccesoRegistro(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=10, max=25)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8, max=25)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')