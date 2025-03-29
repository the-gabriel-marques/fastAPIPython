from database.db import conectar

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            idProduto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL 
        )
    """)
    conn.commit()
    conn.close()

def inserir_produtos(nome, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco)"
    "VALUES (?, ?)", (nome, preco))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def excluir_produtos(idProduto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (idProduto))
    conn.commit()
    conn.close()

def buscar_produtos_por_id(idProduto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (idProduto))
    produto = cursor.fetchone()
    conn.close()
    return produto

def atualizar_produto(idProduto, nome, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE produtos SET nome = ?, preco = ? "
    "WHERE id = ?", (nome, preco, idProduto))
    conn.commit()
    conn.close()