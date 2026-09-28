# Zomato Data & AI Engineering Platform

An end-to-end data engineering and AI engineering project built around Zomato restaurant, customer, order, menu, and review data.

The project combines **Snowflake, dbt, Apache Airflow, Python, Docker, Streamlit, and OpenAI** to demonstrate modern data warehousing, ELT transformation, pipeline orchestration, and AI-powered analytics.

---

## Project Overview

This project transforms raw Zomato datasets into structured analytical models in Snowflake and exposes the resulting data through both traditional analytics and AI-powered interfaces.

The platform follows this general flow:

```text
Raw Zomato Data
       │
       ▼
   Snowflake
       │
       ▼
     dbt
       │
       ├── Staging Models
       │
       └── Analytical Marts
              │
              ├───────────────┐
              ▼               ▼
         Airflow           AI Layer
       Orchestration       Text-to-SQL
                           Review AI / RAG
              │               │
              └───────┬───────┘
                      ▼
               Business Insights
```

---

## Technology Stack

| Technology         | Purpose                                            |
| ------------------ | -------------------------------------------------- |
| **Snowflake**      | Cloud data warehouse                               |
| **dbt**            | SQL transformation and data modelling              |
| **Apache Airflow** | Pipeline orchestration                             |
| **Python**         | Data engineering and AI applications               |
| **Docker**         | Containerized Airflow environment                  |
| **Streamlit**      | Interactive AI/data applications                   |
| **OpenAI**         | Natural-language analytics and review intelligence |
| **SQL**            | Data transformation and analytics                  |
| **Git/GitHub**     | Version control                                    |

---

## Data

The project works with Zomato-style datasets covering:

* Users
* Restaurants
* Food
* Menu
* Orders
* Order Items
* Reviews

The full source datasets are intentionally excluded from the GitHub repository because of their size.

---

# Data Engineering

## Snowflake

Snowflake serves as the central analytical data warehouse.

The project separates raw/source data from transformed analytical models, allowing the transformation layer to be managed independently from the underlying source data.

---

## dbt

dbt is used to build the transformation and modelling layer.

### Staging Models

The staging layer standardizes and prepares the source data for downstream analytics.

```text
stg_users
stg_restaurants
stg_food
stg_menu
stg_orders
stg_order_items
stg_reviews
```

### Analytical Models

The mart layer provides business-oriented models for analysis.

```text
dim_customer
dim_date
dim_food
dim_restaurants

fct_orders
fct_order_items

mart_daily_city_revenune
mart_delivery_sla
mart_restaurant_performance
mart_review_insights
```

The project uses dimensional modelling concepts such as **fact tables, dimension tables, and analytical marts**.

---

# Pipeline Orchestration

## Apache Airflow

Apache Airflow is used to orchestrate the data pipeline.

The Airflow environment runs through Docker Compose and contains the services required to execute and manage the workflow.

The project includes a `zomato_batch` DAG responsible for coordinating pipeline execution.

The orchestration layer separates individual pipeline activities and their dependencies from the transformation logic implemented in dbt.

---

# AI Engineering

The project extends the traditional data platform with an AI layer.

## Natural Language to SQL

The Text-to-SQL application allows users to ask questions about the analytical data using natural language.

For example:

```text
What are the top 10 cities by GMV?
```

The application converts the natural-language request into SQL and executes the query against Snowflake.

This provides a conversational interface for exploring analytical data without requiring users to manually write SQL.

---

## Review Intelligence

The project includes AI processing for restaurant reviews.

Review data can be enriched using language-model-based processing and embeddings, creating a foundation for semantic search and retrieval-based analysis.

---

## RAG

The project includes a Retrieval-Augmented Generation workflow that combines retrieved information with an AI model to provide context-aware responses.

This demonstrates how structured warehouse data and unstructured review information can be incorporated into an AI-enabled analytics platform.

---

# Project Structure

```text
zomato-data-engineering-ai-engineering/
│
├── ai/
│   ├── enrich_reviews.py
│   ├── rag_chat.py
│   ├── test_snowflake.py
│   └── text_to_sql.py
│
├── airflow/
│   ├── dags/
│   │   └── zomato_batch.py
│   ├── Dockerfile
│   └── docker-compose.yaml
│
├── zomato/
│   ├── macros/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   ├── dbt_project.yml
│   └── mfa_test.py
│
├── .gitignore
└── README.md
```

---

# Key Engineering Concepts

This project demonstrates practical experience with:

* Cloud data warehousing
* ELT architecture
* SQL transformation
* Dimensional modelling
* Fact and dimension tables
* dbt staging and mart layers
* Incremental data transformations
* Pipeline orchestration
* Dockerized development
* Python data engineering
* Snowflake connectivity
* Natural-language-to-SQL
* Embeddings
* Retrieval-Augmented Generation
* AI-assisted analytics
* Git-based version control

---

# Running the Project

## Prerequisites

The project requires:

* Python
* Docker Desktop
* Git
* Snowflake account
* dbt
* OpenAI API access

## Environment Variables

Credentials are supplied through local environment variables and `.env` files.

Typical variables include:

```text
SNOWFLAKE_ACCOUNT
SNOWFLAKE_USER
SNOWFLAKE_PRIVATE_KEY_PASSPHRASE
DBT_PRIVATE_KEY_PASSPHRASE
OPENAI_API_KEY
```

**Never commit `.env` files, API keys, passwords, or private keys to GitHub.**

---

## dbt

Navigate to the dbt project:

```powershell
cd zomato
```

Validate the dbt configuration:

```powershell
dbt debug
```

Parse the project:

```powershell
dbt parse
```

Run the transformations:

```powershell
dbt run
```

---

## Airflow

Navigate to the Airflow directory:

```powershell
cd airflow
```

Start the Docker environment:

```powershell
docker compose up -d
```

The Airflow environment can then be used to orchestrate the Zomato pipeline.

---

# Security

Sensitive credentials and generated artifacts are intentionally excluded from version control.

The repository `.gitignore` excludes items such as:

```text
.env
*.p8
*.key
airflow/secret/
airflow/logs/
target/
dbt_packages/
data/
*.log
```

This keeps credentials, private keys, large source datasets, and generated files outside the Git repository.

---

# Project Objective

The objective of this project is to demonstrate an end-to-end approach to building a modern data and AI platform:

```text
                 DATA
                   │
                   ▼
              SNOWFLAKE
                   │
                   ▼
                  DBT
                   │
                   ▼
              DATA MARTS
                   │
          ┌────────┴────────┐
          ▼                 ▼
       AIRFLOW              AI
     ORCHESTRATION      TEXT-TO-SQL
                         RAG / NLP
          │                 │
          └────────┬────────┘
                   ▼
             INSIGHTS
```

The project brings together data engineering, analytics engineering, orchestration, and AI engineering in a single workflow.

---

## Author

**Abiola Soyoye**

Business Intelligence | Data Engineering | AI Engineering

GitHub: [@abiola0071](https://github.com/abiola0071)
