from django.urls import path
from . import views

# modelo = path('endereço/', views.funcao, name='apelido')

urlpatterns = [
    path('', views.home, name='home'), #URL vazia, chama a função home apelido 'home'
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'), #URL /adicionar/x/ chama a função adicionar_ao_carrinho 
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'), #URL /carrinho/ chama a função ver_carrinho
    path('finalizar/', views.finalizar_pedido, name='finalizar_pedido'), #URL 'finalizar/', chama a função finalizar_pedido
]