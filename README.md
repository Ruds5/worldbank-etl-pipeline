
# World Bank ETL Pipeline

An end-to-end ETL pipeline that extracts World Bank indicators,
transforms them using pandas, and loads them into DuckDB for analysis.

## Architecture
Extract → Transform → Load → Analyze

## Data Sources
- World Bank API (GDP per capita, population)

## Key Insights
- Monaco, Liechtenstein, and Luxembourg lead GDP per capita rankings.
- High GDP per capita does not imply large population size.
- DuckDB enables fast analytical queries on local data.

## How to Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m src.pipeline
