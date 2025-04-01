# Importa a classe base FlaskForm da extensão Flask-WTF, que facilita a criação de formulários web com validações.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, Email, EqualTo, Length

# Criação do formulário de login, herdando de FlaskForm
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])   
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

# Criação do formulário de cadastro, também herdando de FlaskForm
class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Cadastrar')
