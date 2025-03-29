from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import products_model

templates = Jinja2Templates(directory="templates")

products_model.criar_tabela()

def mostrar_produtos(request: Request):
    produtos = products_model.listar_produtos()
    return templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})

def mostrar_edicao(request: Request, idProduto: int):
    produto = products_model.buscar_produtos_por_id(idProduto)
    produtos = products_model.listar_produtos()
    return templates.TemplateResponse("produtos/editar.html", {"request": request, "produto": produto, "produtos": produtos})

async def cadastrar_produto(request: Request, nome: str = Form(...), preco: str = Form(...)):
    products_model.inserir_produtos(nome, preco)
    return RedirectResponse("/", status_code=303)

def excluir_produto(idProduto: int):
    products_model.excluir_produtos(idProduto)
    return RedirectResponse("/", status_code=303)

async def atualizar_produto(request: Request, idProduto: int, nome: str = Form(...), preco: str = Form(...)):
    products_model.atualizar_produto(idProduto, nome, preco)
    return RedirectResponse("/", status_code=303)