from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app import db, bcrypt
from app.models import Usuario
from app.forms import LoginForm, CadastroForm

auth = Blueprint('auth', __name__)