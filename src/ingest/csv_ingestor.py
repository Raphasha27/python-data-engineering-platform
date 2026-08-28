"""CSV data ingestor"""
import pandas as pd
from pathlib import Path
from typing import Optional


class CSVIngestor:
    def __init__(self, source_dir: str = "data"):
        self.source_dir = Path(source_dir)
    
    def ingest(self, filename: str) -> pd.DataFrame:
        filepath = self.source_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        df = pd.read_csv(filepath)
        print(f"Ingested {len(df)} rows from {filename}")
        return df
    
    def ingest_all(self) -> pd.DataFrame:
        dfs = []
        for csv_file in self.source_dir.glob("*.csv"):
            dfs.append(self.ingest(csv_file.name))
        return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
