-- SQL script that ranks country origins of band
-- second task
SELECT origin, COUNT(fans) as nb_fans 
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
