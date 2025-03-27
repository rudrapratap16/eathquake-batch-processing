SELECT
    place,
    COUNT(*) AS earthquake_count
FROM
    TABLE_ID
GROUP BY
    place
ORDER BY
    earthquake_count DESC
LIMIT 10