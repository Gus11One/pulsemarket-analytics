import pandas as pd
from datetime import datetime

def validate_order_items(df: pd.DataFrame) -> pd.DataFrame:
    # (df: pd.DataFrame): Espera recibir un objeto DataFrame
    # -> pd.DataFrame: Al terminar devolverá otro DataFrame
    """
    Flags invalid quantities and prices in order items.
    """
    df = df.copy()

    df["valida_quantity"] = (df["quantity"] > 0) & (df["quantity"] <= 100)
    df["validate_price"] = df["unit_price"] > 0

    return df

def validate_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates order status and dates.
    """
    df = df.copy()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce") 
    # Erros no para el programa genera para las fechas invalidas -> NaT

    today = pd.Timestamp(datetime.today().date())

    # datetime.today() trae la información al milisegundo, date() solo extrae la fecha

    df["valid_status"] = df["order_status"].str.lower() == "completed"
    df["valid_order_date"] = df["order_date"] <= today

    return df

def validate_sellers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates seller commission rates.
    """
    df = df.copy()
    df["valid_commission"] = (df["commission_rate"] >= 0) & (df["commission_rate"] <= 1)
    return df

