"""
Rotas de autenticação (login, registro, logout, change-password)
Blueprint para gerenciar autenticação de usuários
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from forms import LoginForm, RegisterForm, ChangePasswordForm
from datetime import datetime
from sqlalchemy.exc import IntegrityError

# Criar um blueprint para autenticação
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login - Autentica o usuário"""
    
    # Se usuário já está logged in, redireciona para home
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        # Buscar usuário pelo email
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data):
            # Login bem-sucedido
            login_user(user, remember=form.remember.data)
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            flash(f'Bem-vindo de volta, {user.username}! 👊', 'success')
            
            # Redirecionar para página anterior ou para home
            next_page = request.args.get('next')
            if next_page and next_page.startswith('/'):
                return redirect(next_page)
            return redirect(url_for('home'))
        else:
            # Email ou senha incorretos
            flash('Email ou senha incorretos. Tente novamente.', 'danger')
    
    return render_template('login.html', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Página de registro - Cria nova conta de usuário"""
    
    # Se usuário já está logged in, redireciona para home
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegisterForm()
    
    if form.validate_on_submit():
        try:
            # Criar novo usuário
            user = User(
                username=form.username.data,
                email=form.email.data,
                nome_completo=form.username.data,  # Usar username como nome_completo por enquanto
                localizacao='Fortaleza - CE • Brasil',
                foto_perfil='assets/jf.png'
            )
            user.set_password(form.password.data)
            
            # Adicionar ao banco de dados
            db.session.add(user)
            db.session.commit()
            
            flash('Conta criada com sucesso! Agora faça login.', 'success')
            return redirect(url_for('auth.login'))
        
        except IntegrityError:
            db.session.rollback()
            flash('Email ou nome de usuário já registrado.', 'danger')
        except Exception as e:
            db.session.rollback()
            flash('Erro ao criar conta. Tente novamente.', 'danger')
    
    return render_template('register.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    """Logout - Desconecta o usuário"""
    logout_user()
    flash('Você foi desconectado com sucesso.', 'info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    """Alterar senha - Permite que usuário mude sua senha"""
    form = ChangePasswordForm()
    
    if form.validate_on_submit():
        # Verificar senha atual
        if not current_user.check_password(form.old_password.data):
            flash('Senha atual incorreta.', 'danger')
            return redirect(url_for('auth.change_password'))
        
        # Alterar para nova senha
        current_user.set_password(form.new_password.data)
        db.session.commit()
        
        flash('Sua senha foi alterada com sucesso!', 'success')
        return redirect(url_for('profile'))
    
    return render_template('change_password.html', form=form)
