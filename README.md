# Cardápio Digital

Aplicação web desenvolvida em Django para gerenciamento de pedidos de uma confeitaria. O cliente navega pelo catálogo, monta o carrinho e finaliza o pedido diretamente pelo WhatsApp.

---

## Funcionalidades

- Catálogo de produtos com imagens, preços e controle de disponibilidade
- Carrinho de compras persistido via sessão do Django
- Controle de quantidade com detecção automática de origem (home ou carrinho) via `HTTP_REFERER`
- Formatação de preços no padrão brasileiro
- Finalização de pedido com redirecionamento para WhatsApp usando `urllib.parse`
- Sistema de cadastro e login com validação de senha e verificação de usuário duplicado
- Perfil do cliente com telefone e sistema de pontos de fidelidade via `OneToOneField`
- Painel administrativo para gerenciar produtos em tempo real

---

## Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)

---

## Estrutura

```
cardapio-digital/
├── catalogo/        # produtos, carrinho e finalização de pedido
├── usuarios/        # cadastro, login, logout e perfil do cliente
├── templates/       # HTML com Django Template Language
├── static/          # CSS
└── core/            # configurações e URLs principais
```

---

## Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/viniciusroland01/cardapio-digital.git
cd cardapio-digital

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install django pillow

# Rode as migrations
python manage.py migrate

# Crie um superusuário para acessar o admin
python manage.py createsuperuser

# Suba o servidor
python manage.py runserver
```

Acesse `http://127.0.0.1:8000` para o cardápio e `http://127.0.0.1:8000/admin` para cadastrar produtos.
