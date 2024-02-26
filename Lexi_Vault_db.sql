-- This script Creates the database Lexi_Vault_db in the MySQL Server if it doesn't exist

CREATE DATABASE IF NOT EXISTS Lexi_Vault_db;

-- This Switches to the newly created database
USE Lexi_Vault_db;

-- This Creates the table dictionary in the database
CREATE TABLE IF NOT EXISTS dictionary (
    word_id INT AUTO_INCREMENT PRIMARY KEY,
    words VARCHAR(255),
    part_of_speech VARCHAR(255),
    meanings TEXT
);

