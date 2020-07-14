-- join

SELECT c.id, c.name ,s.name FROM cities c JOIN states s on c.state_id = s.id ORDER BY c.id;
