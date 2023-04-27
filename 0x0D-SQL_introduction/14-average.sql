-- script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT second_table FROM hbtn_0c_0
ALTER TABLE second_table
ADD COLUMN average INT
INSERT INTO second_table(average)
	VALUES ( AVG(score));
