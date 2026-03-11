import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST", "localhost")
port = os.getenv("POSTGRES_PORT", "5432")
database = os.getenv("POSTGRES_DB")

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

pasta_csv = os.path.join(os.path.dirname(__file__), 'limpos')  # relativo ao script

arquivos_csv = [f for f in os.listdir(pasta_csv) if f.endswith('.csv')]

print(f'Foram encontrados {len(arquivos_csv)} arquivos para importar.\n')

for arquivo in arquivos_csv:
    caminho = os.path.join(pasta_csv, arquivo)
    nome_tabela = os.path.splitext(arquivo)[0].lower()
    
    print(f'📥 Importando {arquivo} para tabela "{nome_tabela}"...')
    try:
        df = pd.read_csv(caminho, encoding='utf-8-sig')
        df.to_sql(nome_tabela, engine, if_exists='replace', index=False)
        print(f'✅ {arquivo} importado com sucesso ({len(df)} linhas).')
    except Exception as e:
        print(f'❌ Erro ao importar {arquivo}: {e}')

print('\n🏁 Importação concluída!')