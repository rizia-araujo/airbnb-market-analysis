import requests
import pandas as pd
from pathlib import Path
from io import BytesIO

url = "https://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2025-12-15/data/listings.csv.gz"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Baixando arquivo...")

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

if response.status_code == 200:

    df = pd.read_csv(
        BytesIO(response.content),
        compression="gzip"
    )

    Path("data/raw").mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        "data/raw/listings.csv",
        index=False
    )

    print("Arquivo salvo com sucesso!")
    print(f"Total de registros: {len(df)}")

else:
    print("Falha no download")