from flask import Flask, render_template, redirect, url_for, flash, jsonify, request
from flask_login import LoginManager, login_required, current_user, logout_user
from models import db, User, JobApplication
from auth_routes import auth_bp
from config import config

def create_app(config_name='development'):
    """Application factory para criar e configurar a Flask app"""
    app = Flask(__name__)
    
    # Carregar configurações
    app.config.from_object(config[config_name])
    
    # Inicializar extensões
    db.init_app(app)
    
    # Configurar LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, faça login para acessar essa página.'
    login_manager.login_message_category = 'info'
    
    @login_manager.user_loader
    def load_user(user_id):
        """Carregar usuário da sessão"""
        return User.query.get(int(user_id))
    
    # Registrar blueprints
    app.register_blueprint(auth_bp)
    
    # Criar contexto da aplicação para banco de dados
    with app.app_context():
        db.create_all()
    
    # ==================== ROTAS PROTEGIDAS ====================
    
    @app.route('/')
    @login_required
    def home():
        """Página inicial - Requer autenticação"""
        return render_template('index.html', user=current_user)

    @app.route('/connect')
    @login_required
    def connect():
        """Página de conexões - Requer autenticação"""
        return render_template('connect.html', user=current_user)

    @app.route('/explore')
    @login_required
    def explore():
        """Página de exploração - Requer autenticação"""
        return render_template('explore.html', user=current_user)

    @app.route('/profile')
    @login_required
    def profile():
        """Página de perfil - Requer autenticação"""
        return render_template('profile.html', user=current_user)

    @app.route('/model')
    @login_required
    def model():
        """Página do modelo - Requer autenticação"""
        return render_template('model.html', user=current_user)

    @app.route('/curriculum')
    @login_required
    def curriculum():
        """Página de currículo - Requer autenticação"""
        return render_template('curriculum.html', user=current_user)

    @app.route('/world')
    @login_required
    def world():
        """Página de mundo - Requer autenticação"""
        return render_template('world.html', user=current_user)

    @app.route('/future')
    @login_required
    def future():
        """Página de futuro - Requer autenticação"""
        return render_template('future.html', user=current_user)
    
    @app.route('/apply-job', methods=['POST'])
    @login_required
    def apply_job():
        """Candidatar-se a uma vaga"""
        data = request.get_json()
        
        job_title = data.get('job_title')
        company = data.get('company')
        match_score = data.get('match_score', 0)
        
        # Verificar se já se candidatou a esta vaga
        existing = JobApplication.query.filter_by(
            user_id=current_user.id,
            job_title=job_title,
            company=company
        ).first()
        
        if existing:
            return jsonify({
                'success': False,
                'message': f'Você já se candidatou para {job_title} em {company}'
            }), 400
        
        # Criar nova candidatura
        application = JobApplication(
            user_id=current_user.id,
            job_title=job_title,
            company=company,
            match_score=float(match_score),
            status='candidatado'
        )
        
        db.session.add(application)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'✅ Candidatura enviada para {job_title}!'
        }), 201
    
    @app.route('/get-applications')
    @login_required
    def get_applications():
        """Obter todas as candidaturas do usuário"""
        applications = JobApplication.query.filter_by(user_id=current_user.id).order_by(JobApplication.created_at.desc()).all()
        
        return jsonify([{
            'id': app.id,
            'job_title': app.job_title,
            'company': app.company,
            'match_score': app.match_score,
            'status': app.status,
            'created_at': app.created_at.strftime('%d/%m/%Y')
        } for app in applications])
    
    @app.route('/withdraw-application/<int:app_id>', methods=['POST'])
    @login_required
    def withdraw_application(app_id):
        """Cancelar candidatura"""
        application = JobApplication.query.get(app_id)
        
        if not application or application.user_id != current_user.id:
            return jsonify({'success': False, 'message': 'Candidatura não encontrada'}), 404
        
        job_title = application.job_title
        db.session.delete(application)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'❌ Candidatura removida de {job_title}'
        })
    
    # ==================== ROTA DE ERRO ====================
    
    @app.errorhandler(404)
    def not_found(error):
        """Página não encontrada"""
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def server_error(error):
        """Erro interno do servidor"""
        return render_template('500.html'), 500
    
    return app

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
