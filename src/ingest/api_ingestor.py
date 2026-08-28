"""API data ingestor"""
import httpx
import pandas as pd
from typing import Optional


class APIIngestor:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client()
    
    def fetch(self, endpoint: str, params: Optional[dict] = None) -> dict:
        response = self.client.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    
    def to_dataframe(self, endpoint: str, params: Optional[dict] = None) -> pd.DataFrame:
        data = self.fetch(endpoint, params)
        return pd.DataFrame(data)
