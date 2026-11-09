import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 1. Setup Parameters
NUM_TRANSACTIONS = 50000
COUNTRIES = ['USA', 'UK', 'Canada', 'Germany', 'France', 'India', 'Japan', 'Brazil']

print("Generating 50,000 synthetic B2B transactions...")

# 2. Generate Base Data
np.random.seed(42)
transaction_ids = [f"TXN-{100000 + i}" for i in range(NUM_TRANSACTIONS)]
customer_ids = [f"CUST-{random.randint(1000, 2500)}" for _ in range(NUM_TRANSACTIONS)]

start_date = datetime.now() - timedelta(days=365)
dates = [start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59)) for _ in range(NUM_TRANSACTIONS)]

amounts = np.round(np.random.exponential(scale=1500, size=NUM_TRANSACTIONS) + 50, 2)
amounts = np.clip(amounts, 50, 10000)

ip_countries = np.random.choice(COUNTRIES, NUM_TRANSACTIONS, p=[0.4, 0.15, 0.1, 0.05, 0.05, 0.15, 0.05, 0.05])

# 3. Generate AI Scores and True Fraud Flags
ai_risk_scores = np.random.beta(a=2, b=10, size=NUM_TRANSACTIONS)
ai_risk_scores = np.round(ai_risk_scores, 4)

ai_decisions = ['Blocked' if score > 0.85 else 'Approved' for score in ai_risk_scores]

true_fraud_flags = []
for score in ai_risk_scores:
    if score > 0.85:
        is_fraud = np.random.choice([True, False], p=[0.70, 0.30])
    else:
        is_fraud = np.random.choice([True, False], p=[0.01, 0.99])
    true_fraud_flags.append(is_fraud)

# 4. Build DataFrame and Export
df = pd.DataFrame({
    'transaction_id': transaction_ids,
    'customer_id': customer_ids,
    'transaction_date': dates,
    'transaction_amount': amounts,
    'ip_country': ip_countries,
    'ai_risk_score': ai_risk_scores,
    'ai_decision': ai_decisions,
    'true_fraud_flag': true_fraud_flags
})

df.to_csv('transactions.csv', index=False)
print("Success! 'transactions.csv' created with 50,000 records.")