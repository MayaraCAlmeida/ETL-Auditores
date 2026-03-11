import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# --- Carrega variáveis do .env ---
load_dotenv()

# --- Conexão com PostgreSQL usando variáveis do .env ---
usuario = os.getenv("POSTGRES_USER")
senha = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST", "localhost")
porta = os.getenv("POSTGRES_PORT", "5432")
banco = os.getenv("POSTGRES_DB")

engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}")

# --- LER AS TABELAS DO PROJETO AGRO E LIMITAR A 10 REGISTROS ---
categorias = ["bovino", "suino", "aves", "leite"]

for categoria in categorias:
    tabela = f"agro_{categoria}"
    df = pd.read_sql(f'SELECT * FROM {tabela} LIMIT 10', engine)
    print(f"\n📄 10 primeiros registros da categoria {categoria.capitalize()}:")
    print(df)
