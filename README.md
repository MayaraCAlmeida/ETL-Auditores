# Projeto ETL - Cadastro de Auditores #
 
Projeto de ETL (Extract, Transform, Load) desenvolvido em Python para automatizar a extração, limpeza e importação de dados de auditores da CVM para PostgreSQL.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Arquitetura ETL](#arquitetura-etl)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Exemplos de Uso](#exemplos-de-uso)
- [Autor](#autor)

## Sobre o Projeto

Este projeto implementa um pipeline ETL completo para processar dados de cadastro de auditores, realizando:

- Extração: Leitura de arquivos CSV compactados em formato ZIP
- Transformação: Limpeza de dados, tratamento de encoding e validação
- Carga: Importação automatizada para banco de dados PostgreSQL

O objetivo é demonstrar boas práticas em engenharia de dados, incluindo tratamento de erros, gestão de dependências e versionamento de código.

## Arquitetura ETL

```
┌─────────────────┐
│   cad_auditor   │
│     .zip        │  ← Extract
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  limpar_csv     │
│    _zip.py      │  ← Transform
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   limpos/       │
│   *.csv         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  importar_csvs  │
│  _postgres.py   │  ← Load
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   PostgreSQL    │
│    Database     │
└─────────────────┘
```

## Tecnologias Utilizadas

- Python 3.10+ - Linguagem principal
- PostgreSQL 14+ - Banco de dados relacional
- pandas - Manipulação e análise de dados
- SQLAlchemy - ORM para comunicação com o banco
- psycopg2-binary - Driver PostgreSQL
- python-dotenv - Gestão de variáveis de ambiente

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- [PostgreSQL 14+](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/)
- pip (gerenciador de pacotes Python)

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/MayaraCAlmeida/ETL_Auditores.git
cd ETL_Auditores

cd cad_auditor_etl
```

### 2. Crie um ambiente virtual


Windows:
```bash
python -m venv venv
venv\Scripts\activate
```


### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## Configuração

### 1. Configure o PostgreSQL

Crie o banco de dados:

```sql
CREATE DATABASE Meu_Banco2;
```

### 2. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha_aqui
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=Meu_Banco2
```

--- ⚠️ Importante: Nunca compartilhe suas credenciais! O arquivo `.env` já está no `.gitignore`.

### 3. Teste a conexão

```bash
python teste_conexao.py
```

Você deve ver:
```
✅ Conexão bem-sucedida!
Versão do PostgreSQL: PostgreSQL 14.x ...
```

## Como Usar

### Passo 1: Prepare os dados

Coloque o arquivo `cad_auditor.zip` na raiz do projeto ou ajuste o caminho em `limpar_csv_zip.py`.

### Passo 2: Execute o pipeline ETL

2.1. Extrair e limpar os CSVs

```bash
python limpar_csv_zip.py
```

Este script irá:
- Extrair os arquivos CSV do ZIP
- Corrigir problemas de encoding (ISO-8859-1 → UTF-8)
- Remover linhas com formatação incorreta
- Salvar os arquivos limpos na pasta `limpos/`

Saída esperada:
```
Foram encontrados 3 arquivos CSV.

🔹 Processando cad_auditor_pf.csv...
✅ cad_auditor_pf.csv limpo e salvo em limpos\cad_auditor_pf.csv (210 linhas).
```

2.2. Importar para o PostgreSQL

Primeiro, ajuste as credenciais em `importar_csvs_postgres.py` (linhas 6-10):

```python
user = 'postgres'
password = 'sua_senha'
host = 'localhost'
port = '5432'
database = 'Meu_Banco2'
```

Execute:

```bash
python importar_csvs_postgres.py
```

Saída esperada:
```
Foram encontrados 3 arquivos para importar.

📥 Importando cad_auditor_pf.csv para tabela "cad_auditor_pf"...
✅ cad_auditor_pf.csv importado com sucesso (210 linhas).

🎉 Importação concluída!
```

### Passo 3: Consulte os dados

```bash
python "listar os dados da tabela.py"
```

Ou use SQL diretamente:

```sql
SELECT * FROM public.cad_auditor_pf LIMIT 10;
```

## Estrutura do Projeto

```
cad_auditor_etl/
│
├── limpar_csv_zip.py            # Extract & Transform: extrai e limpa CSVs
├── importar_csvs_postgres.py    # Load: importa dados para PostgreSQL
├── listar os dados da tabela.py # Consulta registros do banco
├── teste_conexao.py             # Valida conexão com PostgreSQL
├── POSTGRESS.sql                # Scripts SQL de exemplo
├── requirements.txt             # Dependências Python
├── .env                         # Credenciais (não versionado)
├── .gitignore                   # Arquivos ignorados pelo Git
├── README.md                    # Documentação
│
├── limpos/                      # CSVs processados (gerado)
└── dados/                       # CSVs originais (opcional)
```

## Exemplos de Uso

### Consultar auditores ativos

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:senha@localhost:5432/Meu_Banco2')

df = pd.read_sql("""
    SELECT auditor, sit, dt_ini_sit 
    FROM public.cad_auditor_pf 
    WHERE sit = 'ATIVO'
    ORDER BY dt_ini_sit DESC
    LIMIT 10
""", engine)

print(df)
```

### Estrutura da tabela principal

```sql
CREATE TABLE cad_auditor_pf (
    cd_cvm INTEGER,
    auditor TEXT,
    sit TEXT,
    dt_ini_sit DATE
);
```

## Segurança

- Credenciais são armazenadas em `.env` (não versionado)
- Use `python-dotenv` para carregar variáveis de ambiente
- Nunca faça commit de senhas ou dados sensíveis


## Autor

Mayara C Almeida

- GitHub: [@MayaraCAlmeida](https://github.com/MayaraCAlmeida)
- Projeto desenvolvido para estudo de ETL e engenharia de dados

---

## Licença

Este projeto é de código aberto e está disponível para fins educacionais.