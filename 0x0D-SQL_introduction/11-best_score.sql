-- script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT second_table FROM hbtn_0c_0
WHERE second_table.score >= 10
ORDER BY score DESC;
