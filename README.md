<h1 align="center"> Sistema de Cadastro de Produtos </h1>

<h2 align="center"> Usando FastAPI </h2>

<p align="center">
<img loading="lazy" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/FastAPI_logo.svg/768px-FastAPI_logo.svg.png?20240902201856"/>
</p>

<br>

<p>Este projeto implementa um sistema simples de cadastro de produtos, contendo adição, atualização e exclusão dos produtos, utilizando do FastAPI e do Oracle como Banco de Dados.</p>

<br>

<h2 align="center">⚙️  Tecnologias Utilizadas </h2>
<ul>
  <li>Fast API</li>
  <li>Oracle Database</li>
  <li>HTML5</li>
  <li>Jinja2</li>
</ul>

<br>

<h2 align="center">💻  Estrutura do Projeto </h2>

<p align="center">

├── controllers/ <br>
│   └── products_controller.py  <b># Lógica de controle para manipulação dos produtos</b> <br>
├── database/ <br>
│   └── db.py                  <b># Conexão com o banco de dados Oracle</b> <br>
├── models/ <br>
│   └── products_model.py       <b># Modelos de dados e interações com o banco</b> <br>
├── routes/ <br>
│   └── rotas.py               <b># Rotas da API (FastAPI)</b> <br>
├── templates/ <br>
│   └── produtos/ <br>
│       ├── cadastro.html     <b> # Formulário de cadastro de produtos </b> <br>
│       └── editar.html        <b> # Formulário de edição de produtos </b> <br>
├── .env                       <b> # Arquivo de variáveis de ambiente (com as credenciais do banco) </b> <br>
├── main.py                    <b> # Ponto de entrada do aplicativo FastAPI </b> <br>
├── requirements.txt           <b> # Dependências do projeto </b> <br>
└── README.md                  <b> # Documentação do projeto </b> <br>

</p>

<br>

<h2 align="center">🌐  Como Executar o Projeto? </h2>

<ul>

  <li> <h3>Clone o Repositório</h3> </li>

  ```
git clone https://github.com/the-gabriel-marques/fastAPIPython.git
```

  <li> <h3>Crie o Ambiente Virtual</h3> </li>

  ```
python -m venv venv
```

  <li> <h3>Ative o Ambiente Virtual</h3> </li>

  ```
.\venv\Scripts\activate
```

  <li> <h3>Instale as Dependências</h3> </li>

  ```
pip install -r requirements.txt
```

  <li> <h3>Configure o Banco de Dados</h3> </li>
  <p>Atualize o arquivo .env na raiz do projeto com as credenciais para o banco de dados Oracle</p>

  ```
ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SERVICE_NAME=XEPDB1
ORACLE_USER=(SEU_USER)
ORACLE_PASSWORD=(SUA_SENHA)
```

  <li> <h3>Execute o Servidor</h3> </li>

  ```
python main.py
```

  <li> <h3>Acessando o Front-End</h3> </li>

  <li> <h4>Cadastro de produtos</h4> </li>

  <p>
    - Clique no endereço: http://127.0.0.1:8000/; <br>
    - Utilize o formulário para cadastrar um produto novo no sistema.
  </p>

  <li> <h4>Checar tabelas no Oracle</h4> </li>

  <p>
    - Utilizando a extensão do SQLDeveloper para o Visual Studio Code, estabeleça uma conexão e execute o comando para checar se os produtos foram cadastrados corretamente (Utilize o mesmo comando para checar a tabela quando um item for atualizado ou excluído)
    
  ```
SELECT * FROM produtos;
```

  <li> <h4>Atualização de produtos</h4> </li>

  <p>
    - No Postman estabeleça a conexão através do endpoint: http://127.0.0.1:8000/produtos/update/{idProduto}, juntamente do método PUT e o id do produto que gostaria de atualizar 
    <br>
    <br>
    <img loading="lazy" src="https://github.com/user-attachments/assets/5fce4c7d-85a3-4d2e-947f-5e0b7067ded8"/> 
    <br>
    <br>
    - Selecione o formato 'form-data', e atribua as keys referentes aos attributos, neste caso 'nome' e 'preco'; e atribua os valores que gostaria de atualizar em seguida, após isso pode enviar
    <br>
    <br>
    <img loading="lazy" src="https://github.com/user-attachments/assets/11169698-dff0-450d-8ef0-f5580c9322b9"/> 
    <br>
    <br>

  <li> <h4>Deletar produtos</h4> </li>

  <p>
    - No Postman estabeleça a conexão através do endpoint: http://127.0.0.1:8000/produtos/delete/{idProduto}, juntamente do método DELETE e o id do produto que gostaria de deletar, após isso pode enviar 
    <br>
    <br>
    <img loading="lazy" src="https://github.com/user-attachments/assets/9a67b884-b181-425f-bec1-faa17315f634"/> 
  </p>

</ul>

