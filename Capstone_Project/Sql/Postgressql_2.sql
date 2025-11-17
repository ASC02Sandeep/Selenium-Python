-- SQL OPERATIONS

-- SELECT OPS

-- Get a specific account:
SELECT * FROM accounts WHERE account_id = 'ACCid_here';

-- Display distinct account types
SELECT DISTINCT account_type FROM accounts;

-- Update (UPDATE) — Modify owner 
UPDATE accounts
SET owner = 'Nitish Veni'
WHERE account_id = 'uuid_here';

-- Delete (DELETE) — Remove account (must be empty)
DELETE FROM accounts
WHERE account_id = 'uuid_here' AND balance = 0.00;

-- Truncate Table
TRUNCATE TABLE transactions RESTART IDENTITY CASCADE;
TRUNCATE TABLE accounts RESTART IDENTITY CASCADE;
ALTER SEQUENCE acc_no_seq RESTART WITH 10001;
ALTER SEQUENCE txn_id_seq RESTART WITH 1;


-- Accounts with balance above 5000
SELECT * FROM accounts
WHERE balance > 5000;

-- Accounts with balance below 1000
SELECT * FROM accounts
WHERE balance < 1000;

-- Get all "SAVINGS" accounts
SELECT * FROM accounts
WHERE account_type = 'SAVINGS';

--  Find all transactions of type “WITHDRAW”
SELECT * FROM transactions
WHERE transaction_type = 'WITHDRAW';

-- Accounts sorted by balance (highest to lowest)
SELECT owner, balance FROM accounts
ORDER BY balance DESC;

-- Transactions sorted by latest first
SELECT * FROM transactions
ORDER BY created_at DESC;

-- Count of transactions per type
SELECT transaction_type, COUNT(*) AS total_transactions
FROM transactions
GROUP BY transaction_type;

-- Total deposits made by each customer
SELECT a.owner, SUM(t.amount) AS total_deposits
FROM accounts a
JOIN transactions t ON a.account_id = t.account_id
WHERE t.transaction_type = 'DEPOSIT'
GROUP BY a.owner
ORDER BY total_deposits DESC;

-- Customers who made more than 3 transactions
SELECT a.owner, COUNT(t.transaction_id) AS total_txn
FROM accounts a
JOIN transactions t ON a.account_id = t.account_id
GROUP BY a.owner
HAVING COUNT(t.transaction_id) > 3;

-- Show account with the highest balance
SELECT * FROM accounts
WHERE balance = (SELECT MAX(balance) FROM accounts);

-- Get the second-highest balance
SELECT * FROM accounts
WHERE balance = (
    SELECT MAX(balance) FROM accounts
    WHERE balance < (SELECT MAX(balance) FROM accounts)
);

-- Show today’s transactions
SELECT * FROM transactions
WHERE DATE(created_at) = CURRENT_DATE;

-- Find all customers whose name starts with “N”
SELECT * FROM accounts
WHERE owner ILIKE 'N%';







-- Aggregate
-- Total money in the bank
SELECT SUM(balance) AS total_bank_balance
FROM accounts;

-- Average account balance
SELECT AVG(balance) AS avg_balance
FROM accounts;

-- Highest balance
SELECT MAX(balance) AS highest_balance
FROM accounts;

-- Lowest balance
SELECT MIN(balance) AS lowest_balance
FROM accounts;

-- Number of accounts
SELECT COUNT(*) AS total_accounts
FROM accounts;




-- LEFT JOIN — show all accounts, even those without transactions
-- Use when want to see accounts that haven’t yet done any transaction.
SELECT 
    a.owner,
    a.account_type,
    a.balance,
    t.transaction_type,
    t.amount,
    t.created_at
FROM accounts a
LEFT JOIN transactions t
    ON a.account_id = t.account_id
ORDER BY a.owner;













