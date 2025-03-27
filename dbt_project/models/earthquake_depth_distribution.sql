SELECT
    CASE
        WHEN depth < 100 THEN 'Shallow (<100 km)'
        WHEN depth BETWEEN 100 AND 300 THEN 'Intermediate (100-300 km)'
        WHEN depth > 300 THEN 'Deep (>300 km)'
        ELSE 'Unknown'
    END AS depth_category,
    COUNT(*) AS earthquake_count
FROM
    TABLE_ID
GROUP BY
    depth_category
ORDER BY
    depth_category