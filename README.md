# Cardápio Digital

Aplicação web para uma confeitaria feita em Django. O cliente navega pelo catálogo, monta o carrinho e finaliza o pedido pelo WhatsApp.

Tem sistema de cadastro e login com perfil do cliente, carrinho persistido por sessão e formatação de preços no padrão brasileiro.

---

## Stack

`Python` `Django` `SQLite` `HTML` `CSS`

---

## Como rodar

```bash
git clone https://github.com/viniciusroland01/cardapio-digital.git
cd cardapio-digital

python -m venv venv
venv\Scripts\activate

pip install django pillow

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000` para o cardápio e `/admin` para cadastrar produtos.
