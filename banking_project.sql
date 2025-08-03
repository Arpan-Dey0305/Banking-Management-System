-- 1. Create the database
CREATE DATABASE IF NOT EXISTS DB_NAME;

--Use th database
USE project;

-- 2. Create the BANK table
CREATE TABLE IF NOT EXISTS TABLE_NAME (
    ACCNO INT PRIMARY KEY,
    NAME VARCHAR(50),
    BALANCE INT,
    MOB CHAR(10)
);

