import pandas as pd
from sqlalchemy import create_engine, text
import urllib.parse

# 1. Database Credentials
MYSQL_PASSWORD = "Reddy@9441"  # <--- Put your actual password with the @ here

# 2. Safely encode the password so the @ symbol does not break the connection
encoded_password = urllib.parse.quote_plus(MYSQL_PASSWORD)

print("Connecting to MySQL on port 3306...")

# 3. Connect to MySQL and create the database
engine_server = create_engine(f"mysql+pymysql://root:{encoded_password}@localhost:3306/")
with engine_server.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS fraud_risk"))

# 4. Connect to the new database and load the CSV
engine_db = create_engine(f"mysql+pymysql://root:{encoded_password}@localhost:3306/fraud_risk")
df = pd.read_csv("transactions.csv")

print("Loading 50,000 records into the 'fraud_risk' database... (this takes about 10 seconds)")
df.to_sql("raw_transactions", con=engine_db, if_exists="replace", index=False)

print("Success! Table 'raw_transactions' is fully loaded.")