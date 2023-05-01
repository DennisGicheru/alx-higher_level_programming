--script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- results must be sorted in ASC order by cities.id
-- Do not use JOIN
USE hbtn_0d_usa;
SELECT id, name
FROM cities, states
WHERE states.name = 'California%';
ORDER BY cities.id ASC;
