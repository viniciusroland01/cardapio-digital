from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, default='')
    pontos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.usuario.username} - {self.pontos} pontos'



