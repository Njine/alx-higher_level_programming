-- Lists all cities in the hbtn_0d_usa database with their corresponding state names

-- List cities
SELECT cities.id, cities.name, states.name
FROM states, cities WHERE cities.state_id = states.id
ORDER BY cities.id ASC;