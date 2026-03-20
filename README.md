# ETL - Cadastro de Auditores CVM

Pipeline em Python para extrair, limpar e importar os arquivos de cadastro de auditores da CVM para um banco PostgreSQL.

## O que faz

1. `limpar_csv_zip.py` — abre o `cad_auditor.zip`, lê os CSVs com encoding ISO-8859-1 e separador `;`, e salva versões limpas em UTF-8 na pasta `limpos/`
2. `importar_csvs_postgres.py` — pega os CSVs da pasta `limpos/` e importa cada um como tabela no PostgreSQL
3. `consultar_auditores.py` — consulta as 10 primeiras linhas de cada tabela importada
4. `teste_conexao.py` — testa se a conexão com o banco está funcionando

## Requisitos

- Python 3.10+
- PostgreSQL rodando localmente (ou acessível via rede)

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com suas credenciais:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=nome_do_banco
```

## Como usar

```bash
python teste_conexao.py         # verifica se o banco está acessível
python limpar_csv_zip.py        # extrai e limpa os CSVs
python importar_csvs_postgres.py # importa para o PostgreSQL
python consultar_auditores.py   # confere os dados importados
```

## Estrutura

```
.
├── cad_auditor.zip
├── limpar_csv_zip.py
├── importar_csvs_postgres.py
├── consultar_auditores.py
├── teste_conexao.py
├── requirements.txt
├── .env                  # não versionado
└── limpos/               
```

## Tabelas geradas

- `cad_auditor_pf` — auditores pessoa física (cd_cvm, auditor, sit, dt_ini_sit)
- `cad_auditor_pj` — auditores pessoa jurídica (cd_cvm, cnpj, denom_social, sit, dt_ini_sit, endereço...)
