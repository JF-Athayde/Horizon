# 🔐 Sistema de Autenticação - Horizon

## ✨ Status: ✅ COMPLETO E FUNCIONAL

O Horizon agora possui um **sistema de autenticação completo e integrado** com:
- ✅ Login e Registro de usuários
- ✅ Proteção de rotas com `@login_required`
- ✅ Dados de perfil dinâmicos (não mais hardcoded)
- ✅ Gerenciamento de sessão com Flask-Login
- ✅ Banco de dados SQLite com SQLAlchemy ORM
- ✅ Criptografia de senha com Werkzeug
- ✅ CSRF Protection com Flask-WTF
- ✅ Formulários com validação customizada

---

## 🚀 Como Começar (3 Passos)

### 1️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Inicializar Banco de Dados

```bash
python init_db.py
```

Credenciais de teste:
- **Email:** `jf@example.com`
- **Senha:** `senha123`
- **Username:** `jf`

### 3️⃣ Rodar a Aplicação

```bash
python app.py
```

Acesse: `http://127.0.0.1:5001`

---

## 📁 Arquitetura de Arquivos

```
projeto/
├── app.py                      # Flask app com rotas protegidas
├── models.py                   # Modelos SQLAlchemy (User, Event, Task, etc)
├── auth_routes.py              # Blueprint com autenticação
├── config.py                   # Configurações
├── forms.py                    # WTForms com validações
├── init_db.py                  # Script de inicialização do banco
├── requirements.txt            # Dependências
├── horizon.db                  # Banco SQLite (criado automaticamente)
└── templates/
    ├── login.html              # página de login
    ├── register.html           # Página de registro
    ├── change_password.html    # Alterar senha
    ├── header.html             # Header com current_user
    ├── profile.html            # Perfil com dados dinâmicos
    ├── index.html              # Dashboard dinâmico
    ├── 404.html                # Erro 404
    └── 500.html                # Erro 500
```

---

## 🔄 Fluxo de Autenticação

```
Usuário não autenticado acessa /
    ↓
    └→ Redireciona para /login (decorator @login_required)
    
Acessa /login
    ↓
    └→ Preenche formulário
        ↓
        └→ Se válido:
            • Cria sessão
            • Atualiza last_login
            • Redireciona para dashboard
        
        └→ Se inválido:
            • Mostra erro
            • Usuário tenta novamente

Usuário autenticado (em qualquer página)
    ↓
    ├→ current_user disponível em templates
    ├→ Dados carregados do banco
    └→ Pode acessar todas páginas protegidas
```

---

## 👤 Modelo de Usuário

Todos os dados de perfil estão em **models.py**:

```python
class User(UserMixin, db.Model):
    # Autenticação
    username          # Único
    email             # Único
    password_hash     # Criptografada
    
    # Perfil
    nome_completo
    cargo
    localizacao       # Ex: "Fortaleza - CE • Brasil"
    bio
    foto_perfil       # Path da imagem
    
    # Scores
    score_global      # 0-100
    job_readiness     # 0-100
    conexoes_count    # Número de conexões
    
    # Educação
    nivel_academico   # "Graduação", "Mestrado", etc
    instituicao
    ano_conclusao
    
    # Skills & Idiomas
    idiomas           # "Português, Inglês, Espanhol"
    skills            # "Python, React, SQL"
    
    # Experiência
    experiencia
    projetos
    certificados
    video_apresentacao
    
    # Goals
    interesses        # Comma-separated
    ods_foco          # ODS de foco
    
    # Sistema
    ativo             # Boolean
    created_at        # DateTime
    updated_at        # DateTime
    last_login        # DateTime
```

---

## 🎯 Usar `current_user` em Templates

```html
<!-- Nome do usuário -->
{{ current_user.nome_completo }}

<!-- Cargo -->
{{ current_user.cargo }}

<!-- Email -->
{{ current_user.email }}

<!-- Foto -->
<img src="{{ url_for('static', filename=current_user.foto_perfil) }}">

<!-- Score -->
{{ current_user.score_global }}%

<!-- Idiomas (lista) -->
{% for idioma in current_user.get_idiomas_list() %}
    <span>{{ idioma }}</span>
{% endfor %}

<!-- Skills (lista) -->
{% for skill in current_user.get_skills_list() %}
    <span>{{ skill }}</span>
{% endfor %}

<!-- Interesses (lista) -->
{% for interes in current_user.get_interesses_list() %}
    <span>{{ interes }}</span>
{% endfor %}

<!-- ODS (lista) -->
{% for ods in current_user.get_ods_list() %}
    <span>{{ ods }}</span>
{% endfor %}

<!-- Verificar se autenticado -->
{% if current_user.is_authenticated %}
    Logado como: {{ current_user.username }}
{% else %}
    Não autenticado
{% endif %}
```

---

## 🛡️ Proteger Rotas

```python
from flask_login import login_required

@app.route('/minha-pagina')
@login_required
def minha_pagina():
    return render_template('pagina.html', user=current_user)
```

Se não autenticado → Redireciona para `/login`

---

## 📝 Rotas da Plataforma

| Rota | Método | Protegida | Descrição |
|------|--------|-----------|-----------|
| `/login` | GET/POST | ❌ | Login |
| `/register` | GET/POST | ❌ | Registro |
| `/logout` | GET | ✅ | Logout | 
| `/change-password` | GET/POST | ✅ | Alterar senha |
| `/` | GET | ✅ | Dashboard |
| `/profile` | GET | ✅ | Perfil |
| `/connect` | GET | ✅ | Conexões |
| `/explore` | GET | ✅ | Exploração |
| `/world` | GET | ✅ | Horizon World |
| `/future` | GET | ✅ | Horizon Future |
| `/curriculum` | GET | ✅ | Currículo |
| `/model` | GET | ✅ | Modelo |

---

## 🔐 Segurança Implementada

✅ **Senhas Criptografadas**
- Werkzeug com salt automático
- Hash impossível de reverter

✅ **CSRF Protection**
- Tokens em todos os formulários
- Validação automática

✅ **Validação de Formulários**
- Email válido
- Senhas coincidem no registro
- Username único
- Email único

✅ **Proteção de Rotas**
- @login_required bloqueia acesso
- Redirecionamento automático

✅ **Session Management**
- Cookies HttpOnly
- SameSite protection
- Remember me (30 dias)

---

## 🔄 Registro de Novo Usuário

1. Acessa `/register`
2. Preenche:
   - Username (único)
   - Email (válido e único)
   - Senha
   - Confirmar senha
3. Valida dados
4. Se válido:
   - Cria User com password hasheada
   - Redireciona para `/login`
5. Se inválido:
   - Mostra erro
   - Usuário tenta novamente

---

## 🔑 Login de Usuário

1. Acessa `/login`
2. Preenche:
   - Email
   - Senha
   - Remember me (opcional)
3. Valida credenciais
4. Se válido:
   - Cria sessão
   - Atualiza `last_login`
   - Redireciona para dashboard
5. Se inválido:
   - Mostra "Email ou senha incorretos"
   - Usuário tenta novamente

---

## 🧪 Testando o Sistema

1. Abra navegador em `http://127.0.0.1:5001`
2. Será redirecionado para `/login`
3. Faça login com:
   - Email: `jf@example.com`
   - Senha: `senha123`
4. Veja dashboard com dados dinâmicos
5. Acesse perfil para ver todas informações
6. Clique em "Sair" para fazer logout

---

## 📊 Estrutura do Banco de Dados

### Tabela: users
- id (PK)
- username (UNIQUE)
- email (UNIQUE)
- password_hash
- nome_completo, cargo, localizacao, bio
- foto_perfil
- score_global, job_readiness, conexoes_count
- nivel_academico, instituicao, ano_conclusao
- idiomas, skills
- experiencia, projetos, certificados, video_apresentacao
- interesses, ods_foco
- ativo, created_at, updated_at, last_login

### Tabela: events
- id (PK)
- user_id (FK)
- title, description, data_evento, prioridade, warning

### Tabelas Adicionais
- **tasks** - Tarefas simples
- **flash_notes** - Notas rápidas tipo post-it
- **file_uploads** - Links de arquivos

---

## 🛠️ Customização

### Mudar Redirecionamento após Login

Em `auth_routes.py`:
```python
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # ... validação ...
    login_user(user, remember=form.remember.data)
    return redirect(url_for('home'))  # Mude 'home' aqui
```

### Mudar Mensagem de Login Requerido

Em `app.py`:
```python
login_manager.login_message = 'Sua mensagem aqui'
login_manager.login_message_category = 'warning'  # ou 'danger', 'info'
```

### Adicionar Campo ao User

1. Adicione a `models.py`
2. Execute: `python init_db.py` (recria banco)
3. Use em templates

---

## 🚀 Próximas Funcionalidades

- [ ] Edição de perfil (AJAX)
- [ ] Upload de fotografia
- [ ] Recuperação de senha via email
- [ ] 2FA (Two-Factor Authentication)
- [ ] OAuth (Google, GitHub, LinkedIn)
- [ ] Email de confirmação
- [ ] Sistema de notificações
- [ ] Mensagens entre usuários
- [ ] Recomendações de vagas com IA

---

## 📞 Suporte

**Erro ao fazer login?**
1. Verifique se rodar `python init_db.py`
2. Tente credenciais: jf@example.com / senha123
3. Limpe browser cache

**Erro ImportError?**
1. Instale: `pip install -r requirements.txt`
2. Verifique se `models.py`, `forms.py`, etc estão no diretório raiz

**Banco de dados corrompido?**
```bash
rm horizon.db
python init_db.py
```

---

**Status:** ✅ Autenticação completa e funcional
**Versão:** 1.0
**Última atualização:** 2024

