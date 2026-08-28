"""PostgreSQL storage module"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import pandas as pd
from typing import Optional


class DataLake:
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
    
    def save_dataframe(self, df: pd.DataFrame, table_name: str, if_exists: str = "append"):
        df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)
        print(f"Saved {len(df)} rows to {table_name}")
    
    def query(self, sql: str) -> pd.DataFrame:
        with self.engine.connect() as conn:
            return pd.read_sql(text(sql), conn)
    
    def get_table_info(self, table_name: str) -> dict:
        with self.engine.connect() as conn:
            result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
            count = result.scalar()
            return {"table": table_name, "row_count": count}
