from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Perfil

def cadastro(request):
    if request.method == "POST": #verifica se o formulário foi enviado (post) ou se é só visita a página (get)
        usuario_nome = request.POST.get('username') #pega o valor digitado
        senha = request.POST.get('password')
        confirmacao = request.POST.get('password_confirm')
        telefone = request.POST.get('telefone')

        if senha != confirmacao : #se as senhas forem diferentes, mostra o erro e volta para o cadastro
            messages.error(request, 'As senhas não coincidem')
            return render(request, 'usuarios/cadastro.html')
        
        if User.objects.filter(username=usuario_nome).exists(): #verifica se já existe um usuário com esse nome no banco
            messages.error(request, 'Esse usuário já existe!')
            return render(request,'usuarios/cadastro.html')
        
        usuario = User.objects.create_user(username=usuario_nome, password=senha) #cria o usuário com a senha criptografada e salva na variável  'usuario'
        Perfil.objects.create(usuario=usuario, telefone=telefone, pontos=0) #cria o perfil linkado ao usuário com o telefone e pontos zerados

        messages.success(request, 'Conta criada! Faça login.')
        return redirect ('login')
    
    return render(request, 'usuarios/cadastro.html') #se não for post (usuário só acessou a página), mostra o formulário

def sair(request): #encerra a sessão e redireciona para a home depois de sair
    logout(request)
    return redirect ('home')

