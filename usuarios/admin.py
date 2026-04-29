from django.contrib import admin
from .models import Perfil
import urllib.parse #converção de texto para url
import webbrowser 

@admin.register(Perfil) #registro do model 'Perfil' no admin
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario','telefone','pontos'] #colunas que aparecem na lista do admin
    actions = ['adicionar_ponto'] #ações disponíveis no menu do admin

    def adicionar_ponto(self, request, queryset): #self = refêrencia à própria classe PerfilAdmin / request = o pedido do admin / queryset = perfis que o admin selecionou na lista
        for perfil in queryset: 
            perfil.pontos += 1
            perfil.save()

            mensagem = (
                f'Boas notícias {perfil.usuario.username}! 👋\n\n' #criando a mensagem de confirmação de ponto
                f'✅ Seu pedido foi confirmado com sucesso!\n\n'
                f'⭐ Você ganhou +1 ponto de fidelidade!\n'
                f'📊 Seu saldo atual: {perfil.pontos}/20 pontos\n\n'
                f'💡 A cada 20 pontos você ganha um brinde especial!\n\n'
                f'Obrigado pela preferência! 🙏'
            )

            mensagem_url = urllib.parse.quote(mensagem.encode('utf-8'), safe='') #transforma mensagem em url / safe = incluir emojis
            link = f"https://wa.me/55{perfil.telefone}?text={mensagem_url}"

            webbrowser.open(link) #abre o link no navegador automaticamente

        self.message_user(request, 'Ponto adicionado!') #mensagem de sucesso no painel do admin

    adicionar_ponto.short_description = 'Confirmar pedido (+1 ponto)' #nome da ação que aparece no menu dropdown do admin

    
 

