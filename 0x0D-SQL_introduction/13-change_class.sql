-- script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT second_table FROM hbtn_0c_0
DELETE from second_table
WHERE score <= 5
ORDER BY DESC;
