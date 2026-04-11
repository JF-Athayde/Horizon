# ⚡ Quick Start - Horizon

## Iniciar em 3 Comandos

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Criar banco de dados e usuário de teste
python init_db.py

# 3. Rodar a aplicação
python app.py
```

Acesse: `http://127.0.0.1:5001`

---

## Credenciais de Teste

- **Email:** `jf@example.com`
- **Senha:** `senha123`

---

## O que Está Pronto? ✅

- [x] Sistema de login completo
- [x] Registro de novos usuários
- [x] Proteção de todas as rotas
- [x] Dados de perfil dinâmicos (no banco de dados)
- [x] Dashboard funcional
- [x] Perfil com informações do usuário
- [x] Todas as páginas usando current_user

---

## Estrutura

```
app.py              → Aplicação Flask com rotas protegidas
models.py           → Modelos do banco de dados
auth_routes.py      → Rotas de autenticação
config.py           → Configurações
forms.py            → Formulários WTForms
init_db.py          → Inicializar banco de dados
requirements.txt    → Dependências Python
templates/          → Templates HTML
└── login.html      → Página de login
└── register.html   → Página de registro
└── profile.html    → Perfil com dados dinâmicos
└── index.html      → Dashboard dinâmico
```

---

## Usar Dados do Usuário em Templates

```html
<!-- Nome do usuário -->
{{ current_user.nome_completo }}

<!-- Score -->
{{ current_user.score_global }}%

<!-- Foto -->
<img src="{{ url_for('static', filename=current_user.foto_perfil) }}">

<!-- Idiomas -->
{% for idioma in current_user.get_idiomas_list() %}
    {{ idioma }}
{% endfor %}
```

---

## Proteger Nova Rota

```python
from flask_login import login_required

@app.route('/minha-rota')
@login_required
def minha_rota():
    return render_template('pagina.html', user=current_user)
```

---

## Troubleshooting

**Erro de import?**
```bash
pip install -r requirements.txt
```

**Banco com erro?**
```bash
rm horizon.db
python init_db.py
```

**Não consegue fazer login?**
- Verifique credenciais: jf@example.com / senha123
- Verifique se correu `python init_db.py`

---

## Para Desenvolvedor

1. Adicione novos campos em `models.py`
2. Recrie banco: `rm horizon.db && python init_db.py`
3. Use em templates: `{{ current_user.novo_campo }}`

---

**Versão:** 1.0 ✅  
**Status:** Pronto para desenvolvimento
