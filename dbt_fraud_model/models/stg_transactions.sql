WITH raw_data AS (
    SELECT * FROM {{ source('fraud_risk', 'raw_transactions') }}
)

SELECT 
    transaction_id,
    customer_id,
    CAST(transaction_date AS DATETIME) AS transaction_date,
    CAST(transaction_amount AS DECIMAL(10,2)) AS transaction_amount,
    ip_country,
    CAST(ai_risk_score AS DECIMAL(5,4)) AS ai_risk_score,
    ai_decision,
    true_fraud_flag
FROM raw_data