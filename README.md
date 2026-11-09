<img width="602" height="336" alt="image" src="https://github.com/user-attachments/assets/00a4dccd-f99a-4927-959c-2fbcb1a03342" />

# B2B Payment Fraud & Chargeback Command Center

## Project Overview
This repository contains an end-to-end data analytics pipeline designed to simulate, process, and analyze B2B payment transactions for fraud detection. The project highlights the critical balance between blocking fraudulent transactions and minimizing "false positives"—legitimate revenue wrongfully blocked by over-aggressive AI risk thresholds. 

The resulting custom-designed Power BI dashboard serves as a command center for fraud analysts to interactively adjust AI strictness and instantly see the financial impact on blocked revenue and false positive rates.

## Architecture & Tech Stack
| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Data Generation** | Python 3.13, `pandas`, `Faker` | Generated a realistic dataset of 50,000 synthetic B2B transactions with embedded fraud patterns and AI risk scores. |
| **Database** | MySQL (Local, Port 3306) | Acted as the data warehouse (`fraud_risk` schema) to store raw transaction data. |
| **Data Transformation** | dbt (Data Build Tool) | Executed modular SQL data transformations, moving data from staging (`stg_transactions`) to a production-ready fact table (`fct_fraud_monitoring`). |
| **Analytics & BI** | Power BI Desktop, DAX | Delivered an interactive, dark-themed UI with dynamic "What-If" scenario modeling and cross-filtered visual components. |
| **Version Control** | Git, GitHub | Maintained project scripts, dbt configurations, and documentation. |

## Data Pipeline Workflow

### 1. Synthetic Data Generation (`generate_fraud_data.py`)
Developed a Python script to generate highly realistic, randomized transaction data. The script engineered specific columns to simulate machine learning outputs, notably an `ai_risk_score` (0.0 to 1.0) and a `true_fraud_flag` (Boolean) to establish ground truth for testing. The script loaded this raw data directly into the local MySQL instance.

### 2. Data Modeling & Transformation (dbt)
Configured a dbt project using the `dbt-mysql` adapter to transform the raw data into an analytical schema.
* **`stg_transactions`:** Cleaned raw data, casted appropriate data types, and standardized nomenclature.
* **`fct_fraud_monitoring`:** Built the final materialized fact table optimized for Power BI import, ensuring high query performance for dashboard interactions.

### 3. Business Intelligence & DAX Implementation
Built a custom, manually designed Power BI dashboard tailored for risk management teams. 

**Key Features:**
* **Dynamic AI Risk Slicer (What-If Parameter):** A slider allowing users to adjust the AI's strictness (threshold from 0.00 to 1.00). 
* **Context-Aware DAX Measures:** KPIs like `Fraud_Prevented` and `Revenue_Lost_FP` recalculate instantly based on the slicer position. Example DAX logic:
  ```dax
  Revenue_Lost_FP = 
  CALCULATE(
      SUM('fraud_risk fct_fraud_monitoring'[transaction_amount]),
      FILTER(
          'fraud_risk fct_fraud_monitoring',
          'fraud_risk fct_fraud_monitoring'[ai_risk_score] >= [AI Risk Threshold Value] &&
          'fraud_risk fct_fraud_monitoring'[true_fraud_flag] = FALSE()
      )
  )
  Global Risk Heatmap: Maps geographical transaction volume and flags high-risk clusters using conditional bubble scaling.

Customer Recovery Queue: A detailed matrix providing a directly actionable roster of flagged transactions for manual analyst review.

Business Impact
This project demonstrates the ability to engineer a solution that directly addresses a major business pain point: revenue leakage from false positives. By parameterizing the AI risk threshold, stakeholders can visually optimize their risk model to catch maximum fraud while preserving legitimate B2B revenue streams.

How to Run the Project:

Clone this repository to your local VS Code environment.

Ensure MySQL Server is running on port 3306 and create a blank schema named .fraud_risk

Create a Python virtual environment and install required packages manually ().pip install pandas faker dbt-mysql

Execute  to seed the database.python generate_fraud_data.py

Navigate to the  folder and run  to build the staging and fact models in MySQL.dbt_fraud_modeldbt run

Open your  file in Power BI Desktop and refresh the data connection..pbix


