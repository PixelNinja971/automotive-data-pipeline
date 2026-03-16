# Automotive Manufacturing Data Pipeline

A complete **Data Engineering project** implementing an automated **ETL pipeline** for processing industrial manufacturing data.

The pipeline extracts production data from a dataset, transforms it using Python, loads it into a PostgreSQL database, orchestrates the workflow with Apache Airflow, and visualizes the results using Metabase.

This project reproduces a **typical modern data architecture used in industrial environments**.

---

# Project Overview

Industrial manufacturing systems generate large volumes of operational data such as:

- production volumes
- machine performance
- defect rates
- process efficiency

To make these data usable, companies implement **data pipelines** that:

- collect raw data
- clean and transform it
- store it in databases
- make it accessible for analytics and dashboards

This project demonstrates the implementation of such a pipeline.

---

# Architecture

The pipeline follows a **classic ETL architecture**.
     
     CSV Dataset
        ↓
    Python ETL Pipeline
        ↓
    PostgreSQL Database
        ↓
    Airflow Orchestration
        ↓
     Metabase Dashboard


Infrastructure is fully containerized using **Docker**.

---

# Infrastructure

The project runs using multiple Docker containers:

    postgres
    airflow
    data-pipeline
    metabase


Each container is responsible for a specific component of the architecture.

---

# Technologies Used

| Technology | Purpose |
|--------|--------|
| Python | Data processing |
| Pandas | Data transformation |
| PostgreSQL | Data storage |
| SQLAlchemy | Database connection |
| Docker | Containerization |
| Apache Airflow | Pipeline orchestration |
| Metabase | Data visualization |
| Git / GitHub | Version control |

---

# ETL Pipeline

The ETL pipeline is implemented in Python and follows a modular architecture.
    src/
├ extract.py
├ transform.py
├ load.py
└ main.py


## Extract

Reads the raw dataset.

Example:

```python
df = pd.read_csv("data/manufacturing_defect_dataset.csv")

# Transform
Cleans and prepares the data.

Examples:
    handling missing values
    type conversions
    removing unnecessary columns
    calculating performance indicators

# Load
Loads the processed data into PostgreSQL.
Example:
df.to_sql(
    "manufacturing_production",
    engine,
    if_exists="replace",
    index=False
)    

# Airflow Orchestration

Apache Airflow is used to orchestrate the ETL pipeline.
The pipeline is defined as a DAG (Directed Acyclic Graph).
Pipeline tasks:
    extract
        ↓
    transform
        ↓
    load

Airflow allows:

scheduling
monitoring
logging
task management

Web interface:
http://localhost:8080
