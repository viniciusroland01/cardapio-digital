from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} - R$ {self.preco}'
    

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, default='')
    pontos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.usuario.username} - {self.pontos} pontos'
