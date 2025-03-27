SELECT
    CASE
        WHEN mag BETWEEN 0 AND 2 THEN '0-2'
        WHEN mag BETWEEN 2 AND 4 THEN '2-4'
        WHEN mag BETWEEN 4 AND 6 THEN '4-6'
        WHEN mag BETWEEN 6 AND 8 THEN '6-8'
        WHEN mag >= 8 THEN '8+'
        ELSE 'Unknown'
    END AS magnitude_range,
    COUNT(*) AS earthquake_count
FROM
    TABLE_ID
GROUP BY
    magnitude_range
ORDER BY
    magnitude_range