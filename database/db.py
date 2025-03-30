import oracledb
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Pegar credenciais do ambiente
HOST = os.getenv("ORACLE_HOST")
PORT = os.getenv("ORACLE_PORT")
SERVICE_NAME = os.getenv("ORACLE_SERVICE_NAME")
USER = os.getenv("ORACLE_USER")
PASSWORD = os.getenv("ORACLE_PASSWORD")

# Criar string de conexão
dsn = f"{HOST}:{PORT}/{SERVICE_NAME}"

def conectar():
    try:
        conn = oracledb.connect(user=USER, password=PASSWORD, dsn=dsn)
        return conn
    except oracledb.DatabaseError as e:
        print("Erro ao conectar ao Oracle:", e)
        return None
