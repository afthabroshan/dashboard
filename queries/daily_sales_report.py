Daily_Sales_report_Ryd = """
WITH raw_orders AS (
    SELECT DISTINCT
        so.date_order,
        ct.name::text AS team_name,
        so.amount_untaxed
    FROM
        sale_order_line AS sol
        JOIN sale_order AS so ON sol.order_id = so.id
        JOIN crm_team AS ct ON so.team_id = ct.id
    WHERE
        sol.state = 'sale'
        AND so.date_order BETWEEN '2025-07-01'::date AND '2025-08-01'::date
        and so.company_id = 8 --change company id as per sheets
)
SELECT
    CASE 
        WHEN GROUPING(DATE(date_order)) = 1 THEN 'TOTAL'
        ELSE TO_CHAR(DATE(date_order), 'YYYY-MM-DD')
    END AS "DATE",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'RIYADH 1' THEN amount_untaxed ELSE 0 END) AS "MTR RYD-01",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'RIYADH 2' THEN amount_untaxed ELSE 0 END) AS "MTR RYD-02",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'BURAIDA' THEN amount_untaxed ELSE 0 END) AS "MTR BURAIDA",
--    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'JIZAN ROUTE' THEN amount_untaxed ELSE 0 END) AS "JIZAN",
    SUM(amount_untaxed) AS "TOTAL SALE"
FROM
    raw_orders
GROUP BY ROLLUP (DATE(date_order))
ORDER BY
    DATE(date_order) NULLS LAST;
"""
Daily_Sales_report_Dmm = """
WITH raw_orders AS (
    SELECT DISTINCT
        so.date_order,
        ct.name::text AS team_name,
        so.amount_untaxed
    FROM
        sale_order_line AS sol
        JOIN sale_order AS so ON sol.order_id = so.id
        JOIN crm_team AS ct ON so.team_id = ct.id
    WHERE
        sol.state = 'sale'
        AND so.date_order BETWEEN '2025-07-01'::date AND '2025-08-01'::date
        and so.company_id = 7
        and ct.active = true --change company id as per sheets
)
SELECT
    CASE 
        WHEN GROUPING(DATE(date_order)) = 1 THEN 'TOTAL'
        ELSE TO_CHAR(DATE(date_order), 'YYYY-MM-DD')
    END AS "DATE",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'DAMMAM' THEN amount_untaxed ELSE 0 END) AS "MTR DMM-01",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'AL AHSA (DMM)' THEN amount_untaxed ELSE 0 END) AS "MTR AL AHSA-02",
    SUM(amount_untaxed) AS "TOTAL SALE"
FROM
    raw_orders
GROUP BY ROLLUP (DATE(date_order))
ORDER BY
    DATE(date_order) NULLS LAST;
"""

Daily_Sales_report_AXA = """
WITH raw_orders AS (
    SELECT DISTINCT
        so.date_order,
        ct.name::text AS team_name,
        so.amount_untaxed
    FROM
        sale_order_line AS sol
        JOIN sale_order AS so ON sol.order_id = so.id
        JOIN crm_team AS ct ON so.team_id = ct.id
    WHERE
        sol.state = 'sale'
        AND so.date_order BETWEEN '2025-07-01'::date AND '2025-08-01'::date
        and so.company_id = 9
        and ct.active = true --change company id as per sheets
)
SELECT
    CASE 
        WHEN GROUPING(DATE(date_order)) = 1 THEN 'TOTAL'
        ELSE TO_CHAR(DATE(date_order), 'YYYY-MM-DD')
    END AS "DATE",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'KHAMIS-01' THEN amount_untaxed ELSE 0 END) AS "AXA KHAMIS-01",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'ABHA-02' THEN amount_untaxed ELSE 0 END) AS "AXA ABHA-02",
--    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'BURAIDA' THEN amount_untaxed ELSE 0 END) AS "MTR BURAIDA",
--    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'JIZAN ROUTE' THEN amount_untaxed ELSE 0 END) AS "JIZAN",
    SUM(amount_untaxed) AS "TOTAL SALE"
FROM
    raw_orders
GROUP BY ROLLUP (DATE(date_order))
ORDER BY
    DATE(date_order) NULLS LAST;
"""



Daily_Sales_report_Jed = """
WITH raw_orders AS (
    SELECT DISTINCT
        so.date_order,
        ct.name::text AS team_name,
        so.amount_untaxed
    FROM
        sale_order_line AS sol
        JOIN sale_order AS so ON sol.order_id = so.id
        JOIN crm_team AS ct ON so.team_id = ct.id
    WHERE
        sol.state = 'sale'
        AND so.date_order BETWEEN '2025-07-01'::date AND '2025-08-01'::date
        and so.company_id = 6 --change company id as per sheets
)
SELECT
    CASE 
        WHEN GROUPING(DATE(date_order)) = 1 THEN 'TOTAL'
        ELSE TO_CHAR(DATE(date_order), 'YYYY-MM-DD')
    END AS "DATE",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'JEDDAH-01' THEN amount_untaxed ELSE 0 END) AS "MTR JED-01",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'JEDDAH-02' THEN amount_untaxed ELSE 0 END) AS "MTR JED-02",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'MAKKAH & TAIF ROUTE' THEN amount_untaxed ELSE 0 END) AS "MAKKAH AND TAIF",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'JIZAN ROUTE' THEN amount_untaxed ELSE 0 END) AS "JIZAN",
    SUM(amount_untaxed) AS "TOTAL SALE"
FROM
    raw_orders
GROUP BY ROLLUP (DATE(date_order))
ORDER BY
    DATE(date_order) NULLS LAST;
"""

# Define the SQL query (currently shared)
Daily_Sales_report_DXB = """
WITH raw_orders AS (
    SELECT DISTINCT
        so.date_order,
        ct.name::text AS team_name,
        so.amount_untaxed
    FROM
        sale_order_line AS sol
        JOIN sale_order AS so ON sol.order_id = so.id
        JOIN crm_team AS ct ON so.team_id = ct.id
    WHERE
        sol.state = 'sale'
        AND so.date_order BETWEEN '2025-07-01'::date AND '2025-08-01'::date
        and so.company_id = 1 --change company id as per sheets
)
SELECT
    CASE
        WHEN GROUPING(DATE(date_order)) = 1 THEN 'TOTAL'
        ELSE TO_CHAR(DATE(date_order), 'YYYY-MM-DD')
    END AS "DATE",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'DUBAI' THEN amount_untaxed ELSE 0 END) AS "KSK DXB",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'SHARJAH' THEN amount_untaxed ELSE 0 END) AS "KSK SHARJAH",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'AJMAN' THEN amount_untaxed ELSE 0 END) AS "KSK AJMAN",
    SUM(CASE WHEN team_name::jsonb ->> 'en_US' = 'ABU DHABI' THEN amount_untaxed ELSE 0 END) AS "KSK AUH",
    SUM(amount_untaxed) AS "TOTAL SALE"
FROM
    raw_orders
GROUP BY ROLLUP (DATE(date_order))
ORDER BY
    DATE(date_order) NULLS LAST;
"""