-- a script that lists all bands with Glam Rock as their main style

SELECT band_name,
       (LEAST(IFNULL(split, 2022), 2022) - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY lifespan DESC;

