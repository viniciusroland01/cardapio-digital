from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} - R$ {self.preco}'
    
    def preco_formatado(self):
        return f'R$ {self.preco:,.2f}'.replace(',','X').replace('.',',').replace('X','.')
        

