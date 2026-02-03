import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PROCESSED = BASE_DIR / "data" / "processed"
DATA_METRICS = BASE_DIR / "data" / "metrics"

DATA_METRICS.mkdir(parents=True, exist_ok=True)

# Lectura de Archivos
orders = pd.read_csv(DATA_PROCESSED / "orders_clean.csv")
order_items = pd.read_csv(DATA_PROCESSED / "order_items_clean.csv")
sellers = pd.read_csv(DATA_PROCESSED / "sellers_clean.csv")

# KPIS
total_orders = len(orders)
completed_orders = orders["valid_status"].sum()

revenue_total = order_items["total_price"].sum()
revenue_avg = revenue_total / total_orders

sellers_total = len(sellers)
valid_commission_rate = sellers["valid_commission"].mean()

# Consolidad KPIs en una Tabla
kpis = pd.DataFrame({
    "metric":[
        "total_orders",
        "completed_orders",
        "revenue_total",
        "average_revenue_per_order",
        "total_sellers",
        "pct_valid_seller_commission"
    ],
    "value":[
        total_orders,
        completed_orders,
        revenue_total,
        revenue_avg,
        sellers_total,
        valid_commission_rate
    ]

})

# Guardar Archivo
kpis.to_csv(DATA_METRICS / "kpis.csv", index=False)