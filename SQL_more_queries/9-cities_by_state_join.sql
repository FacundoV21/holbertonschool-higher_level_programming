-- first join
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.sate_id = states.id ORDER BY cities.id ASC;
