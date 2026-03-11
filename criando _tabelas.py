import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Conexão com PostgreSQL usando variáveis do .env
usuario = os.getenv("POSTGRES_USER")
senha = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST", "localhost")
porta = os.getenv("POSTGRES_PORT", "5432")
banco = os.getenv("POSTGRES_DB")

engine = create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')

# Pasta onde estão os CSVs limpos (relativa ao script)
pasta_csv = os.path.join(os.path.dirname(__file__), 'limpos')

# Lista todos os CSVs
arquivos_csv = [f for f in os.listdir(pasta_csv) if f.endswith('.csv')]

for arquivo in arquivos_csv:
    caminho = os.path.join(pasta_csv, arquivo)
    nome_tabela = os.path.splitext(arquivo)[0].lower()  # nome da tabela = nome do CSV

    df = pd.read_csv(caminho, encoding='utf-8-sig')
    df.to_sql(nome_tabela, engine, if_exists='replace', index=False)  # cria ou substitui a tabela
    print(f'✅ {arquivo} importado para a tabela "{nome_tabela}" ({len(df)} linhas)')
