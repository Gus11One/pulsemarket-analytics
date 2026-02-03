import pandas as pd

def transform_orders (df: pd.DataFrame) -> pd.DataFrame:
    """
    Keeps only valid orders for analysis.
    """
    df = df.copy()

    df = df[
        (df["valid_status"]) & 
        (df["valid_order_date"])
        ]
        
    return df

def transform_order_items(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keeps only valid order items.
    """
    df = df.copy()
    
    df = df[
        (df["valida_quantity"]) &
        (df["validate_price"])
    ]

    # Convertir a numérico por seguridad
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    

    df["total_price"] = df["quantity"] * df["unit_price"]

    return df

def transform_sellers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keeps sellers with valid commission rates.
    """

    df = df.copy()

    df = df[df["valid_commission"]]

    return df