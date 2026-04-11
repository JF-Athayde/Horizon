from flask_wtf import FlaskForm
from wtforms import (
    StringField, TextAreaField, SubmitField, FileField, PasswordField,
    BooleanField, DateTimeLocalField, SelectField
)
from wtforms.validators import DataRequired, Length, Optional, Email, EqualTo, ValidationError
from flask_wtf.file import FileAllowed
from models import User


# Formulário de login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email é obrigatório'),
        Email(message='Insira um email válido'),
        Length(max=120)
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message='Senha é obrigatória'),
        Length(min=6, message='Senha deve ter pelo menos 6 caracteres')
    ])
    remember = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')


# Formulário de registro de novo usuário
class RegisterForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[
        DataRequired(message='Nome de usuário é obrigatório'),
        Length(min=3, max=80, message='Nome deve ter entre 3 e 80 caracteres')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Email é obrigatório'),
        Email(message='Insira um email válido'),
        Length(max=120)
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message='Senha é obrigatória'),
        Length(min=6, message='Senha deve ter pelo menos 6 caracteres')
    ])
    confirm_password = PasswordField('Confirmar Senha', validators=[
        DataRequired(message='Confirmação de senha é obrigatória'),
        EqualTo('password', message='As senhas devem ser iguais')
    ])
    submit = SubmitField('Registrar')
    
    def validate_email(self, email):
        """Valida se email já está registrado"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este email já está registrado. Use outro email ou faça login.')
    
    def validate_username(self, username):
        """Valida se username já existe"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este nome de usuário já existe. Escolha outro.')


# Formulário de edição de perfil
class ProfileForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[
        DataRequired(message='Nome de usuário é obrigatório'),
        Length(min=3, max=80, message='Nome deve ter entre 3 e 80 caracteres')
    ])
    cargo = StringField('Cargo', validators=[
        Optional(),
        Length(max=50, message='Cargo não pode ter mais de 50 caracteres')
    ])
    bio = TextAreaField('Biografia', validators=[
        Optional(),
        Length(max=500, message='Biografia não pode ter mais de 500 caracteres')
    ])
    photo = FileField('Foto de perfil', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], message='Somente imagens JPG, PNG e GIF são permitidas')
    ])
    submit = SubmitField('Salvar alterações')
    
    def validate_username(self, username):
        """Valida se username já existe (excluindo o usuário atual)"""
        user = User.query.filter_by(username=username.data).first()
        if user and user.id != current_user.id:
            raise ValidationError('Este nome de usuário já existe. Escolha outro.')


# Formulário de change password (alterar senha)
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Senha Atual', validators=[
        DataRequired(message='Digite sua senha atual')
    ])
    new_password = PasswordField('Nova Senha', validators=[
        DataRequired(message='Digite uma nova senha'),
        Length(min=6, message='Nova senha deve ter pelo menos 6 caracteres')
    ])
    confirm_password = PasswordField('Confirmar Nova Senha', validators=[
        DataRequired(message='Confirme a nova senha'),
        EqualTo('new_password', message='As senhas devem ser iguais')
    ])
    submit = SubmitField('Alterar Senha')


# Formulário de criação de evento no calendário
class CalendarForm(FlaskForm):
    title = StringField("Título", validators=[
        DataRequired(message='Título é obrigatório'),
        Length(max=150)
    ])
    description = TextAreaField("Descrição", validators=[
        Optional(),
        Length(max=1000)
    ])
    data = DateTimeLocalField("Data e Hora", format="%Y-%m-%dT%H:%M", validators=[
        DataRequired(message='Data e hora são obrigatórias')
    ])
    prioridade = SelectField("Prioridade", choices=[
        ("1", "Muito Baixa"),
        ("2", "Baixa"),
        ("3", "Média"),
        ("4", "Alta"),
        ("5", "Muito Alta")
    ], validators=[DataRequired()], default="3")
    warning = BooleanField("Aviso / Lembrete")
    submit = SubmitField("Adicionar Evento")


# Formulário para tarefas simples
class TaskForm(FlaskForm):
    description = StringField('Descrição', validators=[
        DataRequired(message='Descrição é obrigatória'),
        Length(min=3, max=300, message='Descrição deve ter entre 3 e 300 caracteres')
    ])
    submit = SubmitField('Adicionar')


# Formulário para upload de links de arquivos
class FileUploadForm(FlaskForm):
    title = StringField('Título do Arquivo', validators=[
        DataRequired(message='Título é obrigatório'),
        Length(max=150)
    ])
    link = StringField('Link do Arquivo', validators=[
        DataRequired(message='Link é obrigatório'),
        Length(max=500, message='Link não pode ter mais de 500 caracteres')
    ])
    description = TextAreaField('Descrição', validators=[
        Optional(),
        Length(max=500)
    ])
    submit = SubmitField('Salvar Arquivo')


# Formulário para criar notas rápidas (tipo post-it)
class FormFlashNotes(FlaskForm):
    content = StringField('Nota', validators=[
        DataRequired(message='Nota não pode estar vazia'),
        Length(min=2, max=500, message='Nota deve ter entre 2 e 500 caracteres')
    ])
    submit = SubmitField('Adicionar')


# Formulário de request password reset
class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email é obrigatório'),
        Email(message='Insira um email válido')
    ])
    submit = SubmitField('Solicitar Reset de Senha')
    
    def validate_email(self, email):
        """Valida se email existe na base de dados"""
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Não existe conta com esse email. Registre-se primeiro.')


# Formulário de reset password
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Nova Senha', validators=[
        DataRequired(message='Senha é obrigatória'),
        Length(min=6, message='Senha deve ter pelo menos 6 caracteres')
    ])
    confirm_password = PasswordField('Confirmar Senha', validators=[
        DataRequired(message='Confirmação de senha é obrigatória'),
        EqualTo('password', message='As senhas devem ser iguais')
    ])
    submit = SubmitField('Redefinir Senha')
