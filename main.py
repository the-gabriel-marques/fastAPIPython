from fastapi import FastAPI #importa a classe que cria a aplicação web
from routes.rotas import router #importa o roteador

app = FastAPI() #app vai servir como o o servidor da API
app.include_router(router) #adiciona o roteadir na aplicação, isso vai permitir que todas as rotas do arquivo rotas.py sejam registradas na API

if __name__ == "__main__": #o código dentro do if só vai ser executado se o arquivo for rodado diretamente
    import uvicorn #usado para rodar aplicações FastAPI
    uvicorn.run(app, host="127.0.0.1", port=8000) #inicia o servidor localmente

#Esse código inicia o servidor fastAPI na porta 8000, acessa as rotas do arquivo rotas.py e os endpoints podem ser acessados pleo navegador ou com o postman por exemplo.