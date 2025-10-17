-- This script populates a db table with one row

USE DATABASE();

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (1, "Cole Baidoo", "cbaidoo@sandtech.com", "123 Happiness Ave.");
