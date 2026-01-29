# PulseMarket Analytics Pipeline

## Overview
End-to-end data analytics project simulating a real e-commerce environment.
The project covers data ingestion, validation, transformation, and business metrics generation.

## Tech Stack
- Python
- Pandas
- Git
- Modular pipeline architecture

## Project Structure
pulsemarket-analytics/
├── data/
│ ├── raw/ # Original source data (immutable)
│ ├── staging/ # Validated data with quality flags
│ ├── processed/ # Cleaned and enriched datasets
│ └── metrics/ # Business KPIs
│
├── notebooks/
│ └── business_analysis.ipynb
│
├── src/
│ ├── main.py # Pipeline orchestrator
│ ├── validate.py # Data quality checks
│ ├── transform.py # Data cleaning & enrichment
│ └── metrics.py # KPI generation
│
├── README.md
├── requirements.txt
└── .gitignore

## What This Project Demonstrates

- Data validation and quality checks
- Layered data pipeline design
- Business-oriented KPI definition
- Analytical thinking and storytelling
- Git best practices
