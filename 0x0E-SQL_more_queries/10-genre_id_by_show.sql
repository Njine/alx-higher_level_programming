-- Lists all cities in the hbtn_0d_usa database with their corresponding state names

-- List cities
SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
