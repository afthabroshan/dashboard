sales_man_monthly_DXB = """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 1
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""


sales_man_monthly_APEX= """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 2
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""



sales_man_monthly_Main_land = """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 3
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""



sales_man_monthly_Muscut = """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 4
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""



sales_man_monthly_Bahrine = """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 5
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""



sales_man_monthly_Jeddah = """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 6
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""



sales_man_monthly_dammam = """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 7
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""



sales_man_monthly_riyadh = """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 8
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""



sales_man_monthly_axa = """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 9
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""


sales_man_monthly_salah = """
SELECT
    'MAIN LAND' AS region_branch,
    STRING_AGG(DISTINCT rp.name, ', ') AS sales_men,
    COALESCE(am.name, 'Unassigned Route') AS route_name,

    -- Monthly Sales
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

    SUM(so.amount_total) AS total_amount

FROM sale_order so
LEFT JOIN area_master am ON so.area_id = am.id
LEFT JOIN res_users ru ON so.user_id = ru.id
LEFT JOIN res_partner rp ON ru.partner_id = rp.id

WHERE so.company_id = 10
  AND so.state IN ('sale', 'done')
  AND so.date_order >= '2025-01-01' AND so.date_order <= '2025-12-31'

GROUP BY am.name
ORDER BY total_amount DESC;"""