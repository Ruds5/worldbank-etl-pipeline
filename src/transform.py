# src/transform.py
import pandas as pd

def transform_indicator(df: pd.DataFrame, new_column_name: str) -> pd.DataFrame:
    """
    Cleans and renames a single indicator.
    """
    df = df.rename(columns={"value": new_column_name})
    df["year"] = df["year"].astype(int)
    df = df.dropna(subset=[new_column_name])
    return df

def merge_indicators(dfs: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Merge multiple indicator DataFrames on iso3 and year.
    """
    merged = None
    for df in dfs.values():
        if merged is None:
            merged = df
        else:
            merged = merged.merge(df, on=["iso3", "year"], how="outer")
    return merged
