WITH ExtractedPercentual AS (
    SELECT
        CASE
            WHEN e.description LIKE '%ref Token #%'
            THEN SUBSTRING_INDEX(SUBSTRING_INDEX(e.description, 'ref Token #', -1), ' ', 1)
            WHEN e.description LIKE '%ref Contrato #%'
            THEN SUBSTRING_INDEX(SUBSTRING_INDEX(e.description, 'ref Contrato #', -1), ' ', 1)
            ELSE NULL
        END AS ref_number,
        CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(e.description, 'Percentual de recompra de ', -1), '%', 1) AS DECIMAL(10, 8)) AS percentual_recompra,
        CAST(REPLACE(REPLACE(REPLACE(c.cpf, '.', ''), '-', ''), ' ', '') AS CHAR) AS client_cpf
    FROM
        extract e
    JOIN
        clients c ON e.id_client = c.id_client
    WHERE
        e.description LIKE '%Percentual de recompra%'
)

SELECT
    ref_number,
    SUM(percentual_recompra) AS total_percentual_recompra,
    client_cpf
FROM
    ExtractedPercentual
WHERE
    ref_number IS NOT NULL
GROUP BY
    ref_number, client_cpf
ORDER BY
    ref_number;
