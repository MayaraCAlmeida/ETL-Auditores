import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

usuario = os.getenv("POSTGRES_USER")
senha = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST", "localhost")
porta = os.getenv("POSTGRES_PORT", "5432")
banco = os.getenv("POSTGRES_DB")

engine = create_engine(
    f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}"
)

for tabela in ["cad_auditor_pf", "cad_auditor_pj"]:
    df = pd.read_sql(f"SELECT * FROM {tabela} LIMIT 10", engine)
    print(f"\n{tabela}:")
    print(df.to_string(index=False))
