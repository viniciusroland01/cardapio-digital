from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

# modelo = path('endereço/', views.funcao, name='apelido')

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'), #página de login pronta do django
    path('sair/', views.sair, name='sair')

]