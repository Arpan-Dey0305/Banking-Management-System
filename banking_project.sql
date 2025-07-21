-- 1. Create the database
CREATE DATABASE IF NOT EXISTS project;
USE project;

-- 2. Create the BANK table
CREATE TABLE IF NOT EXISTS BANK (
    ACCNO INT PRIMARY KEY,
    NAME VARCHAR(50),
    BALANCE INT,
    MOB CHAR(10)
);

-- 3. Insert initial data
INSERT INTO BANK (ACCNO, NAME, BALANCE, MOB) VALUES
(101, 'Arpan Dey', 4500, '8710042392'),
(102, 'Chandana Dey', 3000, '8617092123');
