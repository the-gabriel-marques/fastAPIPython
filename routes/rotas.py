from fastapi import APIRouter, Request
from controllers import  products_controller

router = APIRouter()

@router.get("/")
def pagina_inicial(request: Request):
    return products_controller.mostrar_produtos(request)

@router.get("/produtos/edit/{idProduto}")
def editar_produto(request: Request, idProduto: int):
    return products_controller.mostrar_edicao(request, idProduto)

@router.post("/produtos")
async def cadastrar(request: Request):
    form = await request.form()
    return await products_controller.cadastrar_produto(request, nome=form["nome"], preco=form["preco"])

@router.put("/produtos/update/{idProduto}")
async def atualizar(request: Request, idProduto: int):
    form = await request.form()
    return await products_controller.atualizar_produto(request, idProduto, nome=form["nome"], preco=form["preco"])

@router.delete("/produtos/delete/{idProduto}")
def deletar(idProduto: int):
    return products_controller.excluir_produto(idProduto)

