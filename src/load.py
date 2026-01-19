# src/load.py
import duckdb
import pandas as pd

def init_db(db_path: str = "data/worldbank.duckdb") -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB connection.
    """
    conn = duckdb.connect(db_path)
    return conn

def save_to_duckdb(conn: duckdb.DuckDBPyConnection, df: pd.DataFrame, table_name: str):
    """
    Save DataFrame to DuckDB table.
    """
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM df
    """)
