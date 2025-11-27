total_sales_report_Oman = """
SELECT
    -- 1. Static Region
    'OMAN' AS region_branch,

    -- 2. Sales Man (Hardcoded based on Route ID)
    CASE 
        WHEN so.area_id IN (907, 908, 909) THEN 'NIHAL'
        WHEN so.area_id IN (910, 911, 913, 914, 1018) THEN 'SHIJIN'
        ELSE 'UNKNOWN' 
    END AS sales_man,
    
    -- 3. Route Name
    COALESCE(am.name, 'Unknown Route') AS route_name,

    -- 4. Monthly Sales Breakdown for 2025
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 1 THEN so.amount_total ELSE 0 END) AS jan_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 2 THEN so.amount_total ELSE 0 END) AS feb_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 3 THEN so.amount_total ELSE 0 END) AS mar_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 4 THEN so.amount_total ELSE 0 END) AS apr_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 5 THEN so.amount_total ELSE 0 END) AS may_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 6 THEN so.amount_total ELSE 0 END) AS jun_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 7 THEN so.amount_total ELSE 0 END) AS jul_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 8 THEN so.amount_total ELSE 0 END) AS aug_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 9 THEN so.amount_total ELSE 0 END) AS sep_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 10 THEN so.amount_total ELSE 0 END) AS oct_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 11 THEN so.amount_total ELSE 0 END) AS nov_2025,
    SUM(CASE WHEN EXTRACT(MONTH FROM so.date_order) = 12 THEN so.amount_total ELSE 0 END) AS dec_2025,

    -- 5. Total Sales for the Year
    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id

WHERE
    -- Filter for Confirmed Sales
    so.state IN ('sale', 'done')

    -- Filter for Company ID 4 (Main Branch)
    AND so.company_id = 4

    -- Filter for Year 2025
    AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

    -- Filter by Specific Oman Route IDs
    AND so.area_id IN (
        907, 908, 909,          -- Nihal's Routes
        910, 911, 913, 914, 1018 -- Shijin's Routes
    )

GROUP BY
    am.name,
    -- Group by the Salesman Logic
    CASE 
        WHEN so.area_id IN (907, 908, 909) THEN 'NIHAL'
        WHEN so.area_id IN (910, 911, 913, 914, 1018) THEN 'SHIJIN'
        ELSE 'UNKNOWN' 
    END

ORDER BY
    sales_man,
    total_amount DESC;

    """