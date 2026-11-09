WITH staging AS (
    SELECT * FROM {{ ref('stg_transactions') }}
)

SELECT 
    transaction_id,
    customer_id,
    transaction_date,
    transaction_amount,
    ip_country,
    ai_risk_score,
    ai_decision,
    true_fraud_flag,
    CASE 
        WHEN ai_decision = 'Blocked' AND true_fraud_flag = 1 THEN 'True Positive (Fraud Prevented)'
        WHEN ai_decision = 'Blocked' AND true_fraud_flag = 0 THEN 'False Positive (Revenue Lost)'
        WHEN ai_decision = 'Approved' AND true_fraud_flag = 0 THEN 'True Negative (Safe Revenue)'
        WHEN ai_decision = 'Approved' AND true_fraud_flag = 1 THEN 'False Negative (Fraud Missed)'
    END AS ai_performance_category
FROM staging