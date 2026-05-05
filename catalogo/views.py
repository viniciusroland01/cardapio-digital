from django.shortcuts import render, redirect
from .models import Produto
import urllib.parse

def home(request):
    produtos = Produto.objects.filter(disponivel=True) #filtro dos disponíveis
    return render(request, 'catalogo/home.html' , {'produtos': produtos}) #monta a página home.html e manda os produtos pra ela

def adicionar_ao_carrinho(request,produto_id):
    carrinho = request.session.get('carrinho', {}) #carrinho da sessão, se não tiver começa com vazio {}
    id_str = str(produto_id) #converte o id para texto

    carrinho[id_str] = carrinho.get(id_str, 0) + 1 #pega a quantidade total desse produto, ou 0 se não existir e soma 1

    request.session['carrinho'] = carrinho #salva o carrinho atualizado na sessão
    request.session.modified = True #avisa o django que a sessão mudou e precisa ser salva

    return redirect('home') #manda o usuário de volta para a home

def ver_carrinho(request):
    carrinho_sessao = request.session.get('carrinho', {}) #carrinho da sessão, se não tiver começa com vazio {}
    itens_carrinho = [] #lista vazia que vai receber os itens montados
    total_geral = 0 # começa o total em zero

    for produto_id, quantidade in carrinho_sessao.items(): #percorre o carrinho - a cada volta: produto_id=chave, quantidade=valor
        try:
            produto = Produto.objects.get(id=produto_id) #busca o produto no banco pelo id
            qtd = int(quantidade) #garante que a quantidade seja um número inteiro
            subtotal = produto.preco * qtd #calcula o subtotal desse item
            subtotal_formatado = f'R$ {subtotal:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
            total_geral += subtotal #adiciona o subtotal ao total geral
            itens_carrinho.append({
                'produto' : produto,
                'quantidade' : qtd,
                'subtotal' : subtotal_formatado,
            }) #adiciona um dicionário com os dados do item na lista
        except Produto.DoesNotExist: #se o produto não existir, ignora e continua
            pass  

    total_formatado = f'R$ {total_geral:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') #padrão brasileiro do preço

    return render(request, 'catalogo/carrinho.html', {
        'itens' : itens_carrinho,
        'total' : total_formatado,
    }) #monta a página carrinho.html e manda os itens e o total

def finalizar_pedido(request):
    carrinho_sessao = request.session.get('carrinho', {}) #carrinho da sessão
    if not carrinho_sessao:
        return redirect ('home') #se o carrinho estiver vazio,manda para a 'home'
    
    texto = '🛒 NOVO PEDIDO\n\n' #comeca a montar o texto da mensagem
    total = 0 #comeca com o total zero

    for produto_id, quantidade in carrinho_sessao.items(): #percorre o carrinho
        try:
            produto = Produto.objects.get(id=produto_id)
            qtd = int(quantidade)
            subtotal = produto.preco * qtd
            total += subtotal
            texto += f'{qtd}x {produto.nome} - R$ {subtotal} \n' #adiciona uma linha na mensagem com quantidade, nome e subtotal
        except Produto.DoesNotExist:
            pass

    texto += f'\nTotal: R$ {total}' #adiciona o total na mensagem

    request.session['carrinho'] = {} #limpa o carrinho depois de finalizar
    request.session.modified = True

    texto_final = urllib.parse.quote(texto) #converte o texto para formato de url
    link_whatsapp = f'https://wa.me/5532988366586?text={texto_final}'

    return redirect(link_whatsapp) #redireciona para o whatsapp
