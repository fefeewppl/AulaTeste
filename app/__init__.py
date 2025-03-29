from flask import Flask, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.unauthorized_handler
def unauthorized():
    flash("Você precisa estar logado para acessar esta página.", "warning")
    return redirect(request.referrer or url_for('auth.login'))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.auth.routes import auth
    from app.home.routes import home

    app.register_blueprint(auth)
    app.register_blueprint(home)

    return app  
