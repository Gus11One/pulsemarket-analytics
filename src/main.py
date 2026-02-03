import pandas as pd
from pathlib import Path

from validate import (
    validate_order_items,
    validate_orders,
    validate_sellers
)

from transform import (
    transform_orders,
    transform_order_items,
    transform_sellers
)

# Definir Ruta
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_RAW = BASE_DIR / "data" / "raw"
DATA_STAGING = BASE_DIR / "data" / "staging"
DATA_PROCESSED = BASE_DIR / "data" / "processed"

# Crea carpeta por el mismo Pipeline si ya existe, avanza
DATA_STAGING.mkdir(parents=True, exist_ok=True)
DATA_PROCESSED.mkdir(parents=True, exist_ok=True)


# Lectura de CSV
orders = pd.read_csv(DATA_RAW / "orders.csv")
order_items = pd.read_csv(DATA_RAW / "order_items.csv")
sellers = pd.read_csv(DATA_RAW / "sellers.csv")

# Ejecución de las funciones de Validación
order_items_validated = validate_order_items(order_items)
orders_validated = validate_orders(orders)
sellers_validated = validate_sellers(sellers)

# Guardas los Resultados
order_items_validated.to_csv(
    DATA_STAGING / "order_items_validated.csv",
    index=False
)

orders_validated.to_csv(
    DATA_STAGING / "orders_validated.csv",
    index=False
)

sellers_validated.to_csv(
    DATA_STAGING / "sellers_validated.csv",
    index=False
)

# Transformaciones
orders_clean = transform_orders(orders_validated)
order_items_clean = transform_order_items(order_items_validated)
sellers_clean = transform_sellers(sellers_validated)


# Guardas los Resultados Limpios
orders_clean.to_csv(
    DATA_PROCESSED / "orders_clean.csv",
    index=False
)

order_items_clean.to_csv(
    DATA_PROCESSED / "order_items_clean.csv",
    index=False
)

sellers_clean.to_csv(
    DATA_PROCESSED / "sellers_clean.csv",
    index=False
)
