import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST", "localhost")
port = os.getenv("POSTGRES_PORT", "5432")
database = os.getenv("POSTGRES_DB")

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

pasta = os.path.join(os.path.dirname(__file__), 'limpos')
arquivos = [f for f in os.listdir(pasta) if f.endswith('.csv')]

print(f"{len(arquivos)} arquivo(s) para importar.")

for arquivo in arquivos:
    caminho = os.path.join(pasta, arquivo)
    tabela = os.path.splitext(arquivo)[0].lower()
    try:
        df = pd.read_csv(caminho, encoding='utf-8-sig')
        df.to_sql(tabela, engine, if_exists='replace', index=False)
        print(f"  {arquivo} -> tabela '{tabela}' ({len(df)} linhas)")
    except Exception as e:
        print(f"  Erro em {arquivo}: {e}")
