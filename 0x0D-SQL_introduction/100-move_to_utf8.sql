-- MySQL script to convert database and table to UTF-8mb4

-- Set the database character set and collation
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Use the database
USE hbtn_0c_0;

-- Convert the table to UTF-8mb4
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Change the character set and collation for the 'name' column
ALTER TABLE first_table
    MODIFY name VARCHAR(256)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
