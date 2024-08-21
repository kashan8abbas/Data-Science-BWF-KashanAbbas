-- SQLite
SELECT city FROM Cities
SELECT city FROM Cities WHERE country = "Ireland"
SELECT Airports.name, Cities.name, Cities.country FROM Airports JOIN Cities ON Airports.city_id = Cities.id
SELECT Airports.name FROM Airports JOIN Cities ON Airports.city_id = Cities.city WHERE Cities.city = "london" AND Cities.country = "United Kingdom"