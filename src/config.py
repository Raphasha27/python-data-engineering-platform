"""Configuration module"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/data_lake"
    kafka_brokers: str = "localhost:9092"
    spark_master: str = "local[*]"
    
    class Config:
        env_file = ".env"


settings = Settings()
