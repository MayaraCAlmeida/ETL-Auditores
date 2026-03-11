import pandas as pd
import zipfile
import os

# CAMINHO DO ARQUIVO ZIP (relativo ao script)
zip_path = os.path.join(os.path.dirname(__file__), 'cad_auditor.zip')

# PASTA DE SAÍDA (ONDE OS CSVs LIMPOS VÃO SER SALVOS)
output_dir = os.path.join(os.path.dirname(__file__), 'limpos')
os.makedirs(output_dir, exist_ok=True)

# ABRIR O ZIP E PROCESSAR OS CSVs
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    csv_files = [f for f in zip_ref.namelist() if f.endswith('.csv')]
    print(f"\n📦 Foram encontrados {len(csv_files)} arquivos CSV no ZIP.\n")

    for file_name in csv_files:
        print(f"🔹 Processando: {file_name}...")
        try:
            with zip_ref.open(file_name) as f:
                
                # Lê o CSV com encoding e separador padrão
                df = pd.read_csv(
                    f,
                    encoding='ISO-8859-1',  # evita erro de acentuação
                    sep=',',                # separador padrão
                    on_bad_lines='skip'     # ignora linhas com erro
                )

            # Define o caminho de saída relativo
            output_path = os.path.join(output_dir, os.path.basename(file_name))

            # Salva o arquivo limpo em UTF-8
            df.to_csv(output_path, index=False, encoding='utf-8-sig')

            print(f"✅ {file_name} limpo e salvo em:\n   {output_path} ({len(df)} linhas)\n")

        except Exception as e:
            print(f"❌ Erro ao processar {file_name}: {e}\n")
