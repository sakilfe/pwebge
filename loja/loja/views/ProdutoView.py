from django.http import HttpResponse
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone
def list_produto_view(request, id=None):
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")
    #produtos = produtos.filter(Produto__contains=produto )
    produtos = Produto.objects.all()
    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if produto is not None:
        produtos = produtos.filter(Produto=produto)
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if id is not None:
        produtos = produtos.filter(id=id)
    print(produtos)
    return HttpResponse('<h1>id do produto: %s!</h1>' % id)