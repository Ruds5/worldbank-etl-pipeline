# src/pipeline.py
from .extract import extract_indicator
from .transform import transform_indicator, merge_indicators
from .load import init_db, save_to_duckdb

INDICATORS = {
    "gdp_per_capita": "NY.GDP.PCAP.CD",
    "population": "SP.POP.TOTL",
}

def run_pipeline():
    dfs = {}
    for name, code in INDICATORS.items():
        raw_df = extract_indicator(code)
        dfs[name] = transform_indicator(raw_df, name)

    merged = merge_indicators(dfs)

    conn = init_db()
    save_to_duckdb(conn, merged, "world_bank_indicators")

    print(f"Pipeline finished. Loaded {len(merged)} rows.")

if __name__ == "__main__":
    run_pipeline()
