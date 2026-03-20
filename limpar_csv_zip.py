import pandas as pd
import zipfile
import os

zip_path = os.path.join(os.path.dirname(__file__), "cad_auditor.zip")
output_dir = os.path.join(os.path.dirname(__file__), "limpos")
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(zip_path, "r") as z:
    csv_files = [f for f in z.namelist() if f.endswith(".csv")]
    print(f"{len(csv_files)} arquivo(s) encontrado(s) no ZIP.")

    for nome in csv_files:
        with z.open(nome) as f:
            try:
                df = pd.read_csv(f, encoding="ISO-8859-1", sep=";", on_bad_lines="skip")
                destino = os.path.join(output_dir, os.path.basename(nome))
                df.to_csv(destino, index=False, encoding="utf-8-sig")
                print(f"  {nome} -> limpos/ ({len(df)} linhas)")
            except Exception as e:
                print(f"  Erro em {nome}: {e}")
