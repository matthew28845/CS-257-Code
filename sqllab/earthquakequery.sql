-- Locate all earthquakes within a 10 degree box of San Francisco, listing only the top 10 by latitude.
SELECT * FROM earthquakes WHERE latitude BETWEEN 32 AND 42 AND longitude BETWEEN -127 and -117 ORDER BY latitude DESC FETCH FIRST 10 ROWS ONLY;

-- Calculate the average magnitude of all earthquakes within the period
SELECT AVG(mag) FROM earthquakes;

-- Count the number of earthquakes in the period with a magnitude above 5
SELECT COUNT(mag) FROM earthquakes WHERE mag > 5;
