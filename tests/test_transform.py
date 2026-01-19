# tests/test_transform.py
import pandas as pd
from src.transform import transform_indicator

def test_transform_indicator():
    df = pd.DataFrame({
        "iso3": ["USA", "IND"],
        "year": ["2020", "2020"],
        "value": [1000, 500]
    })
    transformed = transform_indicator(df, "gdp")
    assert "gdp" in transformed.columns
    assert transformed["gdp"].dtype == int or transformed["gdp"].dtype == float
