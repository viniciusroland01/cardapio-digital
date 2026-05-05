from django.urls import path 
from . import views

# modelo = path('endereço/', views.funcao, name='apelido')

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'), 
    path('sair/', views.sair, name='sair'),

]