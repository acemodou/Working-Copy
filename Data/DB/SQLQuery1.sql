 SELECT TOP 1 place, magnitude, occurred_on
 FROM dbo.earthquake
 WHERE cause = 'explosion'
 ORDER BY occurred_on DESC;