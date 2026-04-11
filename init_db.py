"""
Script para inicializar o banco de dados e criar um usuário de teste

Uso:
    python init_db.py
"""

from app import create_app
from models import db, User

def init_database():
    """Criar tabelas e usuário de teste"""
    app = create_app(config_name='development')
    
    with app.app_context():
        # Criar todas as tabelas
        db.create_all()
        print("✅ Tabelas do banco de dados criadas!")
        
        # Verificar se usuário de teste já existe
        user = User.query.filter_by(email='jf@example.com').first()
        
        if user:
            print(f"⚠️  Usuário de teste já existe: {user.username}")
        else:
            # Criar usuário de teste
            user = User(
                username='jf',
                email='jf@example.com',
                nome_completo='Fellipe (JF) Athayde',
                cargo='Future Global Leader',
                localizacao='Fortaleza - CE • Brasil',
                bio='Apaixonado por inovação e impacto global',
                foto_perfil='assets/jf.png',
                score_global=72.0,
                job_readiness=85.0,
                conexoes_count=28,
                nivel_academico='Graduação',
                instituicao='IFCE',
                ano_conclusao='2024',
                idiomas='Português (Nativo), Inglês, Espanhol',
                skills='Python, JavaScript, Flask, React, Docker, Git',
                experiencia='Desenvolvedor Full Stack, Consultor de Tecnologia',
                ods_foco='ODS 4 (Educação), ODS 9 (Inovação), ODS 12 (Consumo)'
            )
            user.set_password('senha123')
            
            db.session.add(user)
            db.session.commit()
            
            print(f"✅ Usuário de teste criado com sucesso!")
            print(f"   Email: jf@example.com")
            print(f"   Senha: senha123")
            print(f"   Username: jf")

if __name__ == '__main__':
    init_database()
