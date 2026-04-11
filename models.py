from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """Modelo de usuário para autenticação com todos os dados de perfil"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Informações de Perfil
    nome_completo = db.Column(db.String(120), default='')
    cargo = db.Column(db.String(50), default='')
    localizacao = db.Column(db.String(100), default='Fortaleza - CE • Brasil')
    bio = db.Column(db.Text, default='')
    foto_perfil = db.Column(db.String(255), default='assets/jf.png')
    
    # Score e Estatísticas
    score_global = db.Column(db.Float, default=0.0)
    job_readiness = db.Column(db.Float, default=0.0)
    conexoes_count = db.Column(db.Integer, default=0)
    
    # Dados Acadêmicos
    nivel_academico = db.Column(db.String(100), default='')
    instituicao = db.Column(db.String(150), default='')
    ano_conclusao = db.Column(db.String(4), default='')
    
    # Idiomas (JSON ou String comma-separated)
    idiomas = db.Column(db.Text, default='Português (Nativo)')
    
    # Skills (JSON ou String)
    skills = db.Column(db.Text, default='')
    
    # Experiência Profissional
    experiencia = db.Column(db.Text, default='')
    projetos = db.Column(db.Text, default='')
    certificados = db.Column(db.Text, default='')
    
    # Vídeo de Apresentação
    video_apresentacao = db.Column(db.String(500), default='')
    
    # Temas e ODS
    interesses = db.Column(db.Text, default='')  # Comma-separated
    ods_foco = db.Column(db.Text, default='')  # Comma-separated
    
    # Status
    ativo = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Relacionamentos
    eventos = db.relationship('Event', backref='usuario', lazy=True, cascade='all, delete-orphan')
    tarefas = db.relationship('Task', backref='usuario', lazy=True, cascade='all, delete-orphan')
    notas = db.relationship('FlashNote', backref='usuario', lazy=True, cascade='all, delete-orphan')
    arquivos = db.relationship('FileUpload', backref='usuario', lazy=True, cascade='all, delete-orphan')
    candidaturas = db.relationship('JobApplication', backref='usuario', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Hash da senha do usuário"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica se a senha está correta"""
        return check_password_hash(self.password_hash, password)
    
    def get_skills_list(self):
        """Retorna skills como lista"""
        return [s.strip() for s in self.skills.split(',') if s.strip()] if self.skills else []
    
    def get_idiomas_list(self):
        """Retorna idiomas como lista"""
        return [i.strip() for i in self.idiomas.split(',') if i.strip()] if self.idiomas else []
    
    def get_interesses_list(self):
        """Retorna interesses como lista"""
        return [i.strip() for i in self.interesses.split(',') if i.strip()] if self.interesses else []
    
    def get_ods_list(self):
        """Retorna ODS como lista"""
        return [o.strip() for o in self.ods_foco.split(',') if o.strip()] if self.ods_foco else []
    
    def __repr__(self):
        return f'<User {self.username}>'


class Event(db.Model):
    """Modelo para eventos/compromissos do calendário"""
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    data_evento = db.Column(db.DateTime, nullable=False)
    prioridade = db.Column(db.Integer, default=3)  # 1-5
    warning = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Event {self.title}>'


class Task(db.Model):
    """Modelo para tarefas simples"""
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    completa = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Task {self.description}>'


class FlashNote(db.Model):
    """Modelo para notas rápidas (tipo post-it)"""
    __tablename__ = 'flash_notes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<FlashNote {self.content[:20]}>'


class FileUpload(db.Model):
    """Modelo para upload de links de arquivos"""
    __tablename__ = 'file_uploads'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    link = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<FileUpload {self.title}>'


class JobApplication(db.Model):
    """Modelo para candidaturas a vagas"""
    __tablename__ = 'job_applications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    match_score = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(50), default='candidatado')  # candidatado, entrevista, rejeitado, aceito
    cover_letter = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<JobApplication {self.job_title} at {self.company}>'

