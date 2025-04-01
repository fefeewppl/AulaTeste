from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app import bcrypt
from app.models import Usuario
from app.forms import LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

# Rota de login - aceita métodos GET (para exibir a página) e POST (para processar o login)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  
    if form.validate_on_submit():  # Verifica se o formulário foi enviado e é válido

        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            login_user(user) 
            return redirect(url_for('home.dashboard')) 
        flash('Credenciais inválidas!', 'danger') 
    return render_template('login.html', form=form)

# Rota de logout - exige que o usuário esteja logado
@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()  # Encerra a sessão do usuário
    return redirect(url_for('auth.login'))  # Redireciona para a tela de login
