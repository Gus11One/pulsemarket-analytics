import pandas as pd
from pathlib import Path
from db import engine

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / "data" / "processed"

tables = [
    ("orders_clean.csv", "orders"),
    ("sellers_clean.csv", "sellers"),
    ("order_items_clean.csv", "order_items"),
]

with engine.begin() as conn:
    for file, table in tables:
        path = PROCESSED_DIR / file
        df = pd.read_csv(path)

        if df.empty:
            raise ValueError(f"{file} está vacío")

        df.to_sql(
            name=table,
            con=conn,
            schema="public",
            if_exists="replace",
            index=False
        )

        print(f"✅ {table} cargada ({len(df)} filas)")
