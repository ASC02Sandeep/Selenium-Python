-- ======================================
--  SIMPLE BANKING DATABASE (PostgreSQL)
-- ======================================

-- Create the database
CREATE DATABASE bank_app;

--  After this, CONNECT to "bank_app" manually in pgAdmin
-- There is NO 'USE database' in PostgreSQL.


-- ======================================
-- Create required extensions & sequences
-- ======================================
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- 5-digit account numbers starting from 10001
CREATE SEQUENCE acc_no_seq START 10001 INCREMENT 1;

-- 5-digit transaction IDs starting from 00001
CREATE SEQUENCE txn_id_seq START 1 INCREMENT 1;


-- ======================================
-- ACCOUNTS TABLE
-- ======================================
CREATE TABLE accounts (
    account_id CHAR(5) PRIMARY KEY 
        DEFAULT LPAD(nextval('acc_no_seq')::TEXT, 5, '0'),
    owner VARCHAR(100) NOT NULL,
    account_type VARCHAR(20) CHECK (account_type IN ('SAVINGS', 'CHECKING')),
    balance NUMERIC(12,2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ======================================
-- TRANSACTIONS TABLE
-- ======================================
CREATE TABLE transactions (
    transaction_id CHAR(5) PRIMARY KEY 
        DEFAULT LPAD(nextval('txn_id_seq')::TEXT, 5, '0'),
    account_id CHAR(5) REFERENCES accounts(account_id) ON DELETE CASCADE,
 transaction_type VARCHAR(20) CHECK (transaction_type IN 
        ('CREATE','DEPOSIT','WITHDRAW','TRANSFER_IN','TRANSFER_OUT','UPDATE','DELETE')),
    amount NUMERIC(12,2) DEFAULT 0.00,

    description TEXT,

    related_account CHAR(5),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ======================================
-- SAMPLE DATA INSERT
-- ======================================
INSERT INTO accounts (owner, account_type, balance)
VALUES 
('Sandeep', 'SAVINGS', 1000.00),
('Rahul', 'CHECKING', 500.00)
RETURNING account_id;


-- ======================================
-- DEPOSIT EXAMPLE
-- ======================================
-- Example: Deposit 
UPDATE accounts
SET balance = balance + 500
WHERE account_id = '10001';

INSERT INTO transactions (account_id, transaction_type, amount, description)
VALUES ('10001', 'DEPOSIT', 500, 'Deposited cash');


-- ======================================
-- WITHDRAW EXAMPLE
-- ======================================
-- Example: Withdraw
UPDATE accounts
SET balance = balance - 300
WHERE account_id = '10002' AND balance >= 300;

INSERT INTO transactions (account_id, transaction_type, amount, description)
VALUES ('10002', 'WITHDRAW', 300, 'Cash withdrawal');


-- ======================================
-- TRANSFER EXAMPLE (10001 → 10002)
-- ======================================
DO $$
DECLARE
    --  CHANGE THESE ONLY
    from_id CHAR(5) := '10001';     -- Sender
    to_id   CHAR(5) := '10002';     -- Receiver
    amount  NUMERIC := 500.00;      -- Amount to transfer
BEGIN
    -- Withdraw from sender
    UPDATE accounts 
    SET balance = balance - amount 
    WHERE account_id = from_id AND balance >= amount;

    -- Deposit to receiver
    UPDATE accounts 
    SET balance = balance + amount 
    WHERE account_id = to_id;

    -- Log: Transfer OUT
    INSERT INTO transactions (account_id, transaction_type, amount, description, related_account)
    VALUES (from_id, 'TRANSFER_OUT', amount, 'Transferred to another account', to_id);

    -- Log: Transfer IN
    INSERT INTO transactions (account_id, transaction_type, amount, description, related_account)
    VALUES (to_id, 'TRANSFER_IN', amount, 'Received from another account', from_id);
END $$;



-- ======================================
-- VIEW DATA
-- ======================================
SELECT * FROM accounts;
SELECT * FROM transactions;




