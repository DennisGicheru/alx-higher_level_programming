-- creates the table unique_id on your MySQL server
-- ID needs to be unique and have a value of 1 by default
CREATE TABLE IF NOT EXISTS unique_id(
		id INT NOT NULL DEFAULT '1' UNIQUE,
		name VARCHAR(256);
