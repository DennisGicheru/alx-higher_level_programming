-- lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- results should be sorted in ascending order by cities.id
USE hbtn_0d_usa;
SELECT id,
       name,
       name
FROM cities
JOIN states
ORDER BY cities.id ASC;
