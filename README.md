# 📊 PulseMarket Analytics – Data Pipeline & KPI Materialization

## 📌 Descripción general

**PulseMarket Analytics** es un proyecto de **data analytics end-to-end** que implementa un pipeline de datos reproducible para procesar información transaccional de e-commerce, cargarla en una base de datos PostgreSQL (Neon) y **materializar KPIs clave** para análisis y visualización.

El enfoque del proyecto es **ingenieril y analítico**, priorizando:
- Limpieza y validación de datos
- Buenas prácticas de ETL
- Separación clara entre datos raw, processed y analytics
- Seguridad de credenciales mediante variables de entorno

---

## 🏗️ Arquitectura del proyecto

```
pulsemarket-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── transform/
│   ├── load_processed_to_db.py
│   ├── materialize_kpis.py
│   └── db.py
│
├── notebooks/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologías utilizadas

- Python 3.10+
- Pandas
- SQLAlchemy
- PostgreSQL (Neon)
- Matplotlib
- Git & GitHub

---

## 🔐 Seguridad

Las credenciales se gestionan mediante variables de entorno.
El archivo `.env` está excluido del repositorio.

---

## 🔄 Flujo del pipeline

1. Limpieza de datos
2. Carga a PostgreSQL
3. Materialización de KPIs

---

## 📈 KPIs

- Revenue diario
- Revenue mensual
- Top sellers por revenue
- Número total de órdenes

---

## 🚀 Ejecución

```bash
pip install -r requirements.txt
python src/load_processed_to_db.py
python src/materialize_kpis.py
```

---

## 👤 Autor

**Gustavo Aliaga**
