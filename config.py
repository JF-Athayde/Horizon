import os
from datetime import timedelta


class Config:
    """Configurações base da aplicação"""
    
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-this-in-production'
    
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///horizon.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-Login
    REMEMBER_COOKIE_DURATION = timedelta(days=30)
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
    
    # Flask-WTF
    WTF_CSRF_TIME_LIMIT = None  # Sem limite de tempo para CSRF
    WTF_CSRF_SSL_STRICT = True
    WTF_CSRF_ENABLED = True


class DevelopmentConfig(Config):
    """Configurações para desenvolvimento"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Configurações para produção"""
    DEBUG = False
    TESTING = False
    # Em produção, use banco de dados PostgreSQL
    # SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/horizon'


class TestingConfig(Config):
    """Configurações para testes"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


# Seleção da configuração
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
