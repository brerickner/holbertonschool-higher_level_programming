-- a script that lists all the cities of California that can
-- be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name
FROM hbtn_0d_usa.cities
WHERE cities.state_id IN (
SELECT states.id
FROM hbtn_0d_usa.states
WHERE states.name = 'California')
ORDER BY cities.id ASC;
