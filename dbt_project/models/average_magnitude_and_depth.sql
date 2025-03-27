SELECT
    place,
    AVG(mag) AS average_magnitude,
    AVG(depth) AS average_depth
FROM
    TABLE_ID
GROUP BY
    place
ORDER BY
    average_magnitude DESC