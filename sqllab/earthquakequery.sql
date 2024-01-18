-- Locate all earthquakes within a 10 degree box of Minneapolis.
SELECT * FROM earthquakes WHERE latitude BETWEEN 40 AND 50 AND longitude BETWEEN -87 and -97 ORDER BY latitude DESC;

-- Calculate the average magnitude of all earthquakes within the period
SELECT AVG(mag) FROM earthquakes;

-- Count the number of earthquakes in the period with a magnitude above 5
SELECT COUNT(mag) FROM earthquakes WHERE mag > 5;
