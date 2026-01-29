# PulseMarket Analytics Pipeline

## Overview
End-to-end data analytics project simulating a real e-commerce environment.
The project covers data ingestion, validation, transformation, and business metrics generation.

## Tech Stack
- **Python**
- **Pandas**
- **Pathlib**
- **Git / GitHub**
- **Jupyter Notebook**

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


---

## Data Pipeline Design

The pipeline is divided into clear and reusable layers:

### 1. Raw
- Original CSV files
- No transformations applied
- Acts as a source of truth

### 2. Staging (Validation)
- Data quality checks
- Business rule validation
- Flags invalid records instead of deleting them blindly

### 3. Processed (Transformation)
- Cleaned datasets
- Enriched business columns (e.g. total item amount)
- Ready for analytics and reporting

### 4. Metrics
- Aggregated KPIs
- Business-oriented indicators
- Output-ready for dashboards or SQL ingestion

---

## Key KPIs Generated

- Total number of orders
- Completed orders
- Total revenue
- Average revenue per order
- Total sellers
- Percentage of sellers with valid commission rates

These metrics are exported as a single, business-ready CSV file.

---

## Business Analysis

A dedicated Jupyter Notebook (`business_analysis.ipynb`) provides:

- Key observations from the KPIs
- Identification of financial and operational risks
- Actionable business recommendations
- Clear analytical storytelling aimed at stakeholders

---

## What This Project Demonstrates

- End-to-end data analytics pipeline design
- Strong data validation and quality control practices
- Separation of concerns across pipeline layers
- Business-oriented metric definition
- Analytical thinking and problem-solving
- Clean Git commit history and project organization

---

## How to Run the Project

From the project root:

```bash
python src/main.py
python src/metrics.py
