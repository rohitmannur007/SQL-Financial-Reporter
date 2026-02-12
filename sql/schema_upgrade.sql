-- Drop old tables if exist
DROP TABLE IF EXISTS fact_transactions;
DROP TABLE IF EXISTS dim_customers;

-- Customer dimension table
CREATE TABLE dim_customers AS
SELECT DISTINCT
    CustomerID
FROM cleaned_transactions;

-- Fact table (transactions)
CREATE TABLE fact_transactions AS
SELECT
    TransactionID,
    CustomerID,
    formatted_date,
    TransactionAmount,
    CustAccountBalance
FROM cleaned_transactions;