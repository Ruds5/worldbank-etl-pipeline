# src/extract.py
import pandas as pd
from world_bank_data import get_series

def extract_indicator(indicator_code: str, start_year: int = 2000, end_year: int = 2023) -> pd.DataFrame:
    """
    Extracts a World Bank indicator and normalizes it to:
    iso3 | year | value
    """
    df = get_series(indicator_code, date=f"{start_year}:{end_year}")
    df = df.reset_index()

    # Normalize known structural columns
    rename_map = {}
    for col in df.columns:
        if col.lower() == "year":
            rename_map[col] = "year"
        elif col.lower() in {"country", "country code", "iso3"}:
            rename_map[col] = "iso3"

    df = df.rename(columns=rename_map)

    # Drop known non-metric metadata columns
    drop_cols = [c for c in df.columns if c.lower() in {"series"}]
    df = df.drop(columns=drop_cols, errors="ignore")

    # Now identify the value column (must be the remaining non-key column)
    value_cols = [c for c in df.columns if c not in {"iso3", "year"}]

    if len(value_cols) != 1:
        raise ValueError(f"Could not uniquely identify value column: {df.columns}")

    df = df.rename(columns={value_cols[0]: "value"})

    return df[["iso3", "year", "value"]]
