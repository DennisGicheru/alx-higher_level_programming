--script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- results must be sorted in ASC order by cities.id
-- Do not use JOIN
SELECT id, name
FROM cities
WHERE state_id IN(
		SELECT id
		FROM states
		WHERE name LIKE '%California%')
ORDER BY id ASC;
