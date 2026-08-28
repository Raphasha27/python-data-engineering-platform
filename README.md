# Python Data Engineering Platform

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-3.5-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Kafka](https://img.shields.io/badge/Apache_Kafka-3.7-231F20?style=flat&logo=apachekafka&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24-2496ED?style=flat&logo=docker&logoColor=white)

> End-to-end data engineering platform with Kafka, Spark, and PostgreSQL

## Architecture

```
CSV/API Sources
      │
      ▼
┌─────────────┐
│  Python     │
│  Ingestion  │
└──────┬──────┘
       │
┌──────▼──────┐
│   Kafka     │
│   Streams   │
└──────┬──────┘
       │
┌──────▼──────┐
│   Spark     │
│  Processing │
└──────┬──────┘
       │
┌──────▼──────┐
│ PostgreSQL  │
│  Data Lake  │
└──────┬──────┘
       │
┌──────▼──────┐
│    dbt      │
│ Transform   │
└──────┬──────┘
       │
┌──────▼──────┐
│  Dashboard  │
│  Analytics  │
└─────────────┘
```

## Quick Start

```bash
# Clone repository
git clone https://github.com/Raphasha27/python-data-engineering-platform.git
cd python-data-engineering-platform

# Start services
docker-compose up -d

# Run ingestion
python -m src.ingest.csv_ingestor

# Run transformation
python -m src.transform.spark_jobs
```

## License

MIT License
