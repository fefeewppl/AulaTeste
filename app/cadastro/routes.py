from flask import Blueprint, render_template, redirect, url_for, flash
from app import db, bcrypt
from app.models import Usuario
from app.forms import CadastroForm

cadastro = Blueprint('cadastro', __name__)


@cadastro.route('/cadastro', methods=['GET', 'POST'])
def cadastro_view():
    form = CadastroForm()  # Instancia o formulário de cadastro
    if form.validate_on_submit():  # Se o formulário for enviado e válido
        # Verifica se já existe um usuário com o mesmo e-mail
        usuario_existente = Usuario.query.filter_by(email=form.email.data).first()
        if usuario_existente:
            # Caso já exista, exibe aviso e retorna o formulário preenchido
            flash('E-mail já cadastrado. Por favor, use outro.', 'warning')
            return render_template('cadastro.html', form=form)
        
        # Gera o hash da senha informada
        senha_hash = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')
        
        # Cria uma nova instância de usuário com os dados fornecidos
        usuario = Usuario(
            nome=form.nome.data,
            email=form.email.data,
            senha=senha_hash
        )

        # Adiciona o novo usuário ao banco de dados
        db.session.add(usuario)
        db.session.commit()

        # Exibe mensagem de sucesso e redireciona para o login
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('auth.login'))

    # Exibe o formulário de cadastro
    return render_template('cadastro.html', form=form)
