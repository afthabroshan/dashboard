monthly_sales_report_Bahrain = """
WITH MonthlySales AS (
    -- 1. Get all posted invoice sales for the specified company and year
    SELECT
        am.partner_id,
        EXTRACT(MONTH FROM am.invoice_date) AS sales_month,
        SUM(am.amount_total_in_currency_signed) AS total_sales
    FROM
        account_move AS am
    WHERE
        am.move_type = 'out_invoice'  -- Customer Invoices
        AND am.company_id = 5         -- Your specified company
        AND am.state = 'posted'       -- Only count confirmed invoices
        AND EXTRACT(YEAR FROM am.invoice_date) = 2025 -- Year from your report
    GROUP BY
        am.partner_id, sales_month
),
PivotedSales AS (
    -- 2. Pivot the monthly sales data into columns
    SELECT
        partner_id,
        SUM(CASE WHEN sales_month = 1 THEN total_sales ELSE 0 END) AS "JAN",
        SUM(CASE WHEN sales_month = 2 THEN total_sales ELSE 0 END) AS "FEB",
        SUM(CASE WHEN sales_month = 3 THEN total_sales ELSE 0 END) AS "MAR",
        SUM(CASE WHEN sales_month = 4 THEN total_sales ELSE 0 END) AS "APR",
        SUM(CASE WHEN sales_month = 5 THEN total_sales ELSE 0 END) AS "MAY",
        SUM(CASE WHEN sales_month = 6 THEN total_sales ELSE 0 END) AS "JUN",
        SUM(CASE WHEN sales_month = 7 THEN total_sales ELSE 0 END) AS "JUL",
        SUM(CASE WHEN sales_month = 8 THEN total_sales ELSE 0 END) AS "AUG",
        SUM(CASE WHEN sales_month = 9 THEN total_sales ELSE 0 END) AS "SEP",
        SUM(CASE WHEN sales_month = 10 THEN total_sales ELSE 0 END) AS "OCT",
        SUM(CASE WHEN sales_month = 11 THEN total_sales ELSE 0 END) AS "NOV",
        SUM(CASE WHEN sales_month = 12 THEN total_sales ELSE 0 END) AS "DEC",
        SUM(total_sales) AS "TOTAL"
    FROM
        MonthlySales
    GROUP BY
        partner_id
)
-- 3. Select the partner details and join with the pivoted sales data
SELECT
    ROW_NUMBER() OVER(ORDER BY rp.name) AS "SL NO",
    rp.name AS "COMPANY",
    
    -- --- CHANGED: Fetch Route from CRM Team ---
    -- Using COALESCE to handle cases where name might be JSONB (common in Odoo) or plain text
    COALESCE(ct.name::jsonb ->> 'en_US', ct.name::text) AS "ROUTE", 
    
    -- --- CHANGED: Fetch Location from Area Master ---
    area.name AS "LOCATION",

    COALESCE(ps."JAN", 0) AS "JAN",
    COALESCE(ps."FEB", 0) AS "FEB",
    COALESCE(ps."MAR", 0) AS "MAR",
    COALESCE(ps."APR", 0) AS "APR",
    COALESCE(ps."MAY", 0) AS "MAY",
    COALESCE(ps."JUN", 0) AS "JUN",
    COALESCE(ps."JUL", 0) AS "JUL",
    COALESCE(ps."AUG", 0) AS "AUG",
    COALESCE(ps."SEP", 0) AS "SEP",
    COALESCE(ps."OCT", 0) AS "OCT",
    COALESCE(ps."NOV", 0) AS "NOV",
    COALESCE(ps."DEC", 0) AS "DEC",
    COALESCE(ps."TOTAL", 0) AS "TOTAL"
FROM
    res_partner AS rp
    
-- --- ADDED JOIN 1: Connect Partner to Area Master ---
LEFT JOIN
    area_master AS area ON rp.area_id = area.id

-- --- ADDED JOIN 2: Connect Area Master to CRM Team (Route) ---
LEFT JOIN
    crm_team AS ct ON area.route_id = ct.id

LEFT JOIN
    PivotedSales AS ps ON rp.id = ps.partner_id
WHERE
    -- Only show customers who actually had sales
    COALESCE(ps."TOTAL", 0) > 0
ORDER BY
    "ROUTE"; 

"""

monthly_sales_report_JED = """
WITH MonthlySales AS (
    -- 1. Get all posted invoice sales for the specified company and year
    SELECT
        am.partner_id,
        EXTRACT(MONTH FROM am.invoice_date) AS sales_month,
        SUM(am.amount_total_in_currency_signed) AS total_sales
    FROM
        account_move AS am
    WHERE
        am.move_type = 'out_invoice'  -- Customer Invoices
        AND am.company_id = 6         -- Your specified company
        AND am.state = 'posted'       -- Only count confirmed invoices
        AND EXTRACT(YEAR FROM am.invoice_date) = 2025 -- Year from your report
    GROUP BY
        am.partner_id, sales_month
),
PivotedSales AS (
    -- 2. Pivot the monthly sales data into columns
    SELECT
        partner_id,
        SUM(CASE WHEN sales_month = 1 THEN total_sales ELSE 0 END) AS "JAN",
        SUM(CASE WHEN sales_month = 2 THEN total_sales ELSE 0 END) AS "FEB",
        SUM(CASE WHEN sales_month = 3 THEN total_sales ELSE 0 END) AS "MAR",
        SUM(CASE WHEN sales_month = 4 THEN total_sales ELSE 0 END) AS "APR",
        SUM(CASE WHEN sales_month = 5 THEN total_sales ELSE 0 END) AS "MAY",
        SUM(CASE WHEN sales_month = 6 THEN total_sales ELSE 0 END) AS "JUN",
        SUM(CASE WHEN sales_month = 7 THEN total_sales ELSE 0 END) AS "JUL",
        SUM(CASE WHEN sales_month = 8 THEN total_sales ELSE 0 END) AS "AUG",
        SUM(CASE WHEN sales_month = 9 THEN total_sales ELSE 0 END) AS "SEP",
        SUM(CASE WHEN sales_month = 10 THEN total_sales ELSE 0 END) AS "OCT",
        SUM(CASE WHEN sales_month = 11 THEN total_sales ELSE 0 END) AS "NOV",
        SUM(CASE WHEN sales_month = 12 THEN total_sales ELSE 0 END) AS "DEC",
        SUM(total_sales) AS "TOTAL"
    FROM
        MonthlySales
    GROUP BY
        partner_id
)
-- 3. Select the partner details and join with the pivoted sales data
SELECT
    ROW_NUMBER() OVER(ORDER BY rp.name) AS "SL NO",
    rp.name AS "COMPANY",
    
    -- --- CHANGED: Fetch Route from CRM Team ---
    -- Using COALESCE to handle cases where name might be JSONB (common in Odoo) or plain text
    COALESCE(ct.name::jsonb ->> 'en_US', ct.name::text) AS "ROUTE", 
    
    -- --- CHANGED: Fetch Location from Area Master ---
    area.name AS "LOCATION",

    COALESCE(ps."JAN", 0) AS "JAN",
    COALESCE(ps."FEB", 0) AS "FEB",
    COALESCE(ps."MAR", 0) AS "MAR",
    COALESCE(ps."APR", 0) AS "APR",
    COALESCE(ps."MAY", 0) AS "MAY",
    COALESCE(ps."JUN", 0) AS "JUN",
    COALESCE(ps."JUL", 0) AS "JUL",
    COALESCE(ps."AUG", 0) AS "AUG",
    COALESCE(ps."SEP", 0) AS "SEP",
    COALESCE(ps."OCT", 0) AS "OCT",
    COALESCE(ps."NOV", 0) AS "NOV",
    COALESCE(ps."DEC", 0) AS "DEC",
    COALESCE(ps."TOTAL", 0) AS "TOTAL"
FROM
    res_partner AS rp
    
-- --- ADDED JOIN 1: Connect Partner to Area Master ---
LEFT JOIN
    area_master AS area ON rp.area_id = area.id

-- --- ADDED JOIN 2: Connect Area Master to CRM Team (Route) ---
LEFT JOIN
    crm_team AS ct ON area.route_id = ct.id

LEFT JOIN
    PivotedSales AS ps ON rp.id = ps.partner_id
WHERE
    -- Only show customers who actually had sales
    COALESCE(ps."TOTAL", 0) > 0
ORDER BY
    "ROUTE";
"""

monthly_sales_report_AXA = """
WITH MonthlySales AS (
    -- 1. Get all posted invoice sales for the specified company and year
    SELECT
        am.partner_id,
        EXTRACT(MONTH FROM am.invoice_date) AS sales_month,
        SUM(am.amount_total_in_currency_signed) AS total_sales
    FROM
        account_move AS am
    WHERE
        am.move_type = 'out_invoice'  -- Customer Invoices
        AND am.company_id = 9         -- Your specified company
        AND am.state = 'posted'       -- Only count confirmed invoices
        AND EXTRACT(YEAR FROM am.invoice_date) = 2025 -- Year from your report
    GROUP BY
        am.partner_id, sales_month
),
PivotedSales AS (
    -- 2. Pivot the monthly sales data into columns
    SELECT
        partner_id,
        SUM(CASE WHEN sales_month = 1 THEN total_sales ELSE 0 END) AS "JAN",
        SUM(CASE WHEN sales_month = 2 THEN total_sales ELSE 0 END) AS "FEB",
        SUM(CASE WHEN sales_month = 3 THEN total_sales ELSE 0 END) AS "MAR",
        SUM(CASE WHEN sales_month = 4 THEN total_sales ELSE 0 END) AS "APR",
        SUM(CASE WHEN sales_month = 5 THEN total_sales ELSE 0 END) AS "MAY",
        SUM(CASE WHEN sales_month = 6 THEN total_sales ELSE 0 END) AS "JUN",
        SUM(CASE WHEN sales_month = 7 THEN total_sales ELSE 0 END) AS "JUL",
        SUM(CASE WHEN sales_month = 8 THEN total_sales ELSE 0 END) AS "AUG",
        SUM(CASE WHEN sales_month = 9 THEN total_sales ELSE 0 END) AS "SEP",
        SUM(CASE WHEN sales_month = 10 THEN total_sales ELSE 0 END) AS "OCT",
        SUM(CASE WHEN sales_month = 11 THEN total_sales ELSE 0 END) AS "NOV",
        SUM(CASE WHEN sales_month = 12 THEN total_sales ELSE 0 END) AS "DEC",
        SUM(total_sales) AS "TOTAL"
    FROM
        MonthlySales
    GROUP BY
        partner_id
)
-- 3. Select the partner details and join with the pivoted sales data
SELECT
    ROW_NUMBER() OVER(ORDER BY rp.name) AS "SL NO",
    rp.name AS "COMPANY",
    
    -- --- CHANGED: Fetch Route from CRM Team ---
    -- Using COALESCE to handle cases where name might be JSONB (common in Odoo) or plain text
    COALESCE(ct.name::jsonb ->> 'en_US', ct.name::text) AS "ROUTE", 
    
    -- --- CHANGED: Fetch Location from Area Master ---
    area.name AS "LOCATION",

    COALESCE(ps."JAN", 0) AS "JAN",
    COALESCE(ps."FEB", 0) AS "FEB",
    COALESCE(ps."MAR", 0) AS "MAR",
    COALESCE(ps."APR", 0) AS "APR",
    COALESCE(ps."MAY", 0) AS "MAY",
    COALESCE(ps."JUN", 0) AS "JUN",
    COALESCE(ps."JUL", 0) AS "JUL",
    COALESCE(ps."AUG", 0) AS "AUG",
    COALESCE(ps."SEP", 0) AS "SEP",
    COALESCE(ps."OCT", 0) AS "OCT",
    COALESCE(ps."NOV", 0) AS "NOV",
    COALESCE(ps."DEC", 0) AS "DEC",
    COALESCE(ps."TOTAL", 0) AS "TOTAL"
FROM
    res_partner AS rp
    
-- --- ADDED JOIN 1: Connect Partner to Area Master ---
LEFT JOIN
    area_master AS area ON rp.area_id = area.id

-- --- ADDED JOIN 2: Connect Area Master to CRM Team (Route) ---
LEFT JOIN
    crm_team AS ct ON area.route_id = ct.id

LEFT JOIN
    PivotedSales AS ps ON rp.id = ps.partner_id
WHERE
    -- Only show customers who actually had sales
    COALESCE(ps."TOTAL", 0) > 0
ORDER BY
    "ROUTE";

"""

monthly_sales_report_RUH = """
WITH MonthlySales AS (
    -- 1. Get all posted invoice sales for the specified company and year
    SELECT
        am.partner_id,
        EXTRACT(MONTH FROM am.invoice_date) AS sales_month,
        SUM(am.amount_total_in_currency_signed) AS total_sales
    FROM
        account_move AS am
    WHERE
        am.move_type = 'out_invoice'  -- Customer Invoices
        AND am.company_id = 8         -- Your specified company
        AND am.state = 'posted'       -- Only count confirmed invoices
        AND EXTRACT(YEAR FROM am.invoice_date) = 2025 -- Year from your report
    GROUP BY
        am.partner_id, sales_month
),
PivotedSales AS (
    -- 2. Pivot the monthly sales data into columns
    SELECT
        partner_id,
        SUM(CASE WHEN sales_month = 1 THEN total_sales ELSE 0 END) AS "JAN",
        SUM(CASE WHEN sales_month = 2 THEN total_sales ELSE 0 END) AS "FEB",
        SUM(CASE WHEN sales_month = 3 THEN total_sales ELSE 0 END) AS "MAR",
        SUM(CASE WHEN sales_month = 4 THEN total_sales ELSE 0 END) AS "APR",
        SUM(CASE WHEN sales_month = 5 THEN total_sales ELSE 0 END) AS "MAY",
        SUM(CASE WHEN sales_month = 6 THEN total_sales ELSE 0 END) AS "JUN",
        SUM(CASE WHEN sales_month = 7 THEN total_sales ELSE 0 END) AS "JUL",
        SUM(CASE WHEN sales_month = 8 THEN total_sales ELSE 0 END) AS "AUG",
        SUM(CASE WHEN sales_month = 9 THEN total_sales ELSE 0 END) AS "SEP",
        SUM(CASE WHEN sales_month = 10 THEN total_sales ELSE 0 END) AS "OCT",
        SUM(CASE WHEN sales_month = 11 THEN total_sales ELSE 0 END) AS "NOV",
        SUM(CASE WHEN sales_month = 12 THEN total_sales ELSE 0 END) AS "DEC",
        SUM(total_sales) AS "TOTAL"
    FROM
        MonthlySales
    GROUP BY
        partner_id
)
-- 3. Select the partner details and join with the pivoted sales data
SELECT
    ROW_NUMBER() OVER(ORDER BY rp.name) AS "SL NO",
    rp.name AS "COMPANY",
    
    -- --- CHANGED: Fetch Route from CRM Team ---
    -- Using COALESCE to handle cases where name might be JSONB (common in Odoo) or plain text
    COALESCE(ct.name::jsonb ->> 'en_US', ct.name::text) AS "ROUTE", 
    
    -- --- CHANGED: Fetch Location from Area Master ---
    area.name AS "LOCATION",

    COALESCE(ps."JAN", 0) AS "JAN",
    COALESCE(ps."FEB", 0) AS "FEB",
    COALESCE(ps."MAR", 0) AS "MAR",
    COALESCE(ps."APR", 0) AS "APR",
    COALESCE(ps."MAY", 0) AS "MAY",
    COALESCE(ps."JUN", 0) AS "JUN",
    COALESCE(ps."JUL", 0) AS "JUL",
    COALESCE(ps."AUG", 0) AS "AUG",
    COALESCE(ps."SEP", 0) AS "SEP",
    COALESCE(ps."OCT", 0) AS "OCT",
    COALESCE(ps."NOV", 0) AS "NOV",
    COALESCE(ps."DEC", 0) AS "DEC",
    COALESCE(ps."TOTAL", 0) AS "TOTAL"
FROM
    res_partner AS rp
    
-- --- ADDED JOIN 1: Connect Partner to Area Master ---
LEFT JOIN
    area_master AS area ON rp.area_id = area.id

-- --- ADDED JOIN 2: Connect Area Master to CRM Team (Route) ---
LEFT JOIN
    crm_team AS ct ON area.route_id = ct.id

LEFT JOIN
    PivotedSales AS ps ON rp.id = ps.partner_id
WHERE
    -- Only show customers who actually had sales
    COALESCE(ps."TOTAL", 0) > 0
ORDER BY
    "ROUTE";

"""

monthly_sales_report_DMM = """
WITH MonthlySales AS (
    -- 1. Get all posted invoice sales for the specified company and year
    SELECT
        am.partner_id,
        EXTRACT(MONTH FROM am.invoice_date) AS sales_month,
        SUM(am.amount_total_in_currency_signed) AS total_sales
    FROM
        account_move AS am
    WHERE
        am.move_type = 'out_invoice'  -- Customer Invoices
        AND am.company_id = 7         -- Your specified company
        AND am.state = 'posted'       -- Only count confirmed invoices
        AND EXTRACT(YEAR FROM am.invoice_date) = 2025 -- Year from your report
    GROUP BY
        am.partner_id, sales_month
),
PivotedSales AS (
    -- 2. Pivot the monthly sales data into columns
    SELECT
        partner_id,
        SUM(CASE WHEN sales_month = 1 THEN total_sales ELSE 0 END) AS "JAN",
        SUM(CASE WHEN sales_month = 2 THEN total_sales ELSE 0 END) AS "FEB",
        SUM(CASE WHEN sales_month = 3 THEN total_sales ELSE 0 END) AS "MAR",
        SUM(CASE WHEN sales_month = 4 THEN total_sales ELSE 0 END) AS "APR",
        SUM(CASE WHEN sales_month = 5 THEN total_sales ELSE 0 END) AS "MAY",
        SUM(CASE WHEN sales_month = 6 THEN total_sales ELSE 0 END) AS "JUN",
        SUM(CASE WHEN sales_month = 7 THEN total_sales ELSE 0 END) AS "JUL",
        SUM(CASE WHEN sales_month = 8 THEN total_sales ELSE 0 END) AS "AUG",
        SUM(CASE WHEN sales_month = 9 THEN total_sales ELSE 0 END) AS "SEP",
        SUM(CASE WHEN sales_month = 10 THEN total_sales ELSE 0 END) AS "OCT",
        SUM(CASE WHEN sales_month = 11 THEN total_sales ELSE 0 END) AS "NOV",
        SUM(CASE WHEN sales_month = 12 THEN total_sales ELSE 0 END) AS "DEC",
        SUM(total_sales) AS "TOTAL"
    FROM
        MonthlySales
    GROUP BY
        partner_id
)
-- 3. Select the partner details and join with the pivoted sales data
SELECT
    ROW_NUMBER() OVER(ORDER BY rp.name) AS "SL NO",
    rp.name AS "COMPANY",
    
    -- --- CHANGED: Fetch Route from CRM Team ---
    -- Using COALESCE to handle cases where name might be JSONB (common in Odoo) or plain text
    COALESCE(ct.name::jsonb ->> 'en_US', ct.name::text) AS "ROUTE", 
    
    -- --- CHANGED: Fetch Location from Area Master ---
    area.name AS "LOCATION",

    COALESCE(ps."JAN", 0) AS "JAN",
    COALESCE(ps."FEB", 0) AS "FEB",
    COALESCE(ps."MAR", 0) AS "MAR",
    COALESCE(ps."APR", 0) AS "APR",
    COALESCE(ps."MAY", 0) AS "MAY",
    COALESCE(ps."JUN", 0) AS "JUN",
    COALESCE(ps."JUL", 0) AS "JUL",
    COALESCE(ps."AUG", 0) AS "AUG",
    COALESCE(ps."SEP", 0) AS "SEP",
    COALESCE(ps."OCT", 0) AS "OCT",
    COALESCE(ps."NOV", 0) AS "NOV",
    COALESCE(ps."DEC", 0) AS "DEC",
    COALESCE(ps."TOTAL", 0) AS "TOTAL"
FROM
    res_partner AS rp
    
-- --- ADDED JOIN 1: Connect Partner to Area Master ---
LEFT JOIN
    area_master AS area ON rp.area_id = area.id

-- --- ADDED JOIN 2: Connect Area Master to CRM Team (Route) ---
LEFT JOIN
    crm_team AS ct ON area.route_id = ct.id

LEFT JOIN
    PivotedSales AS ps ON rp.id = ps.partner_id
WHERE
    -- Only show customers who actually had sales
    COALESCE(ps."TOTAL", 0) > 0
ORDER BY
    "ROUTE";

    """

monthly_sales_report_MSCT = """
WITH MonthlySales AS (
    -- 1. Get all posted invoice sales for the specified company and year
    SELECT
        am.partner_id,
        EXTRACT(MONTH FROM am.invoice_date) AS sales_month,
        SUM(am.amount_total_in_currency_signed) AS total_sales
    FROM
        account_move AS am
    WHERE
        am.move_type = 'out_invoice'  -- Customer Invoices
        AND am.company_id = 4         -- Your specified company
        AND am.state = 'posted'       -- Only count confirmed invoices
        AND EXTRACT(YEAR FROM am.invoice_date) = 2025 -- Year from your report
    GROUP BY
        am.partner_id, sales_month
),
PivotedSales AS (
    -- 2. Pivot the monthly sales data into columns
    SELECT
        partner_id,
        SUM(CASE WHEN sales_month = 1 THEN total_sales ELSE 0 END) AS "JAN",
        SUM(CASE WHEN sales_month = 2 THEN total_sales ELSE 0 END) AS "FEB",
        SUM(CASE WHEN sales_month = 3 THEN total_sales ELSE 0 END) AS "MAR",
        SUM(CASE WHEN sales_month = 4 THEN total_sales ELSE 0 END) AS "APR",
        SUM(CASE WHEN sales_month = 5 THEN total_sales ELSE 0 END) AS "MAY",
        SUM(CASE WHEN sales_month = 6 THEN total_sales ELSE 0 END) AS "JUN",
        SUM(CASE WHEN sales_month = 7 THEN total_sales ELSE 0 END) AS "JUL",
        SUM(CASE WHEN sales_month = 8 THEN total_sales ELSE 0 END) AS "AUG",
        SUM(CASE WHEN sales_month = 9 THEN total_sales ELSE 0 END) AS "SEP",
        SUM(CASE WHEN sales_month = 10 THEN total_sales ELSE 0 END) AS "OCT",
        SUM(CASE WHEN sales_month = 11 THEN total_sales ELSE 0 END) AS "NOV",
        SUM(CASE WHEN sales_month = 12 THEN total_sales ELSE 0 END) AS "DEC",
        SUM(total_sales) AS "TOTAL"
    FROM
        MonthlySales
    GROUP BY
        partner_id
)
-- 3. Select the partner details and join with the pivoted sales data
SELECT
    ROW_NUMBER() OVER(ORDER BY rp.name) AS "SL NO",
    rp.name AS "COMPANY",
    
    -- --- CHANGED: Fetch Route from CRM Team ---
    -- Using COALESCE to handle cases where name might be JSONB (common in Odoo) or plain text
    COALESCE(ct.name::jsonb ->> 'en_US', ct.name::text) AS "ROUTE", 
    
    -- --- CHANGED: Fetch Location from Area Master ---
    area.name AS "LOCATION",

    COALESCE(ps."JAN", 0) AS "JAN",
    COALESCE(ps."FEB", 0) AS "FEB",
    COALESCE(ps."MAR", 0) AS "MAR",
    COALESCE(ps."APR", 0) AS "APR",
    COALESCE(ps."MAY", 0) AS "MAY",
    COALESCE(ps."JUN", 0) AS "JUN",
    COALESCE(ps."JUL", 0) AS "JUL",
    COALESCE(ps."AUG", 0) AS "AUG",
    COALESCE(ps."SEP", 0) AS "SEP",
    COALESCE(ps."OCT", 0) AS "OCT",
    COALESCE(ps."NOV", 0) AS "NOV",
    COALESCE(ps."DEC", 0) AS "DEC",
    COALESCE(ps."TOTAL", 0) AS "TOTAL"
FROM
    res_partner AS rp
    
-- --- ADDED JOIN 1: Connect Partner to Area Master ---
LEFT JOIN
    area_master AS area ON rp.area_id = area.id

-- --- ADDED JOIN 2: Connect Area Master to CRM Team (Route) ---
LEFT JOIN
    crm_team AS ct ON area.route_id = ct.id

LEFT JOIN
    PivotedSales AS ps ON rp.id = ps.partner_id
WHERE
    -- Only show customers who actually had sales
    COALESCE(ps."TOTAL", 0) > 0
ORDER BY
    "ROUTE";

    """

monthly_sales_report_Salalah = """
WITH MonthlySales AS (
    -- 1. Get all posted invoice sales for the specified company and year
    SELECT
        am.partner_id,
        EXTRACT(MONTH FROM am.invoice_date) AS sales_month,
        SUM(am.amount_total_in_currency_signed) AS total_sales
    FROM
        account_move AS am
    WHERE
        am.move_type = 'out_invoice'  -- Customer Invoices
        AND am.company_id = 6         -- Your specified company
        AND am.state = 'posted'       -- Only count confirmed invoices
        AND EXTRACT(YEAR FROM am.invoice_date) = 2025 -- Year from your report
    GROUP BY
        am.partner_id, sales_month
),
PivotedSales AS (
    -- 2. Pivot the monthly sales data into columns
    SELECT
        partner_id,
        SUM(CASE WHEN sales_month = 1 THEN total_sales ELSE 0 END) AS "JAN",
        SUM(CASE WHEN sales_month = 2 THEN total_sales ELSE 0 END) AS "FEB",
        SUM(CASE WHEN sales_month = 3 THEN total_sales ELSE 0 END) AS "MAR",
        SUM(CASE WHEN sales_month = 4 THEN total_sales ELSE 0 END) AS "APR",
        SUM(CASE WHEN sales_month = 5 THEN total_sales ELSE 0 END) AS "MAY",
        SUM(CASE WHEN sales_month = 6 THEN total_sales ELSE 0 END) AS "JUN",
        SUM(CASE WHEN sales_month = 7 THEN total_sales ELSE 0 END) AS "JUL",
        SUM(CASE WHEN sales_month = 8 THEN total_sales ELSE 0 END) AS "AUG",
        SUM(CASE WHEN sales_month = 9 THEN total_sales ELSE 0 END) AS "SEP",
        SUM(CASE WHEN sales_month = 10 THEN total_sales ELSE 0 END) AS "OCT",
        SUM(CASE WHEN sales_month = 11 THEN total_sales ELSE 0 END) AS "NOV",
        SUM(CASE WHEN sales_month = 12 THEN total_sales ELSE 0 END) AS "DEC",
        SUM(total_sales) AS "TOTAL"
    FROM
        MonthlySales
    GROUP BY
        partner_id
)
-- 3. Select the partner details and join with the pivoted sales data
SELECT
    ROW_NUMBER() OVER(ORDER BY rp.name) AS "SL NO",
    rp.name AS "COMPANY",
    
    -- --- CHANGED: Fetch Route from CRM Team ---
    -- Using COALESCE to handle cases where name might be JSONB (common in Odoo) or plain text
    COALESCE(ct.name::jsonb ->> 'en_US', ct.name::text) AS "ROUTE", 
    
    -- --- CHANGED: Fetch Location from Area Master ---
    area.name AS "LOCATION",

    COALESCE(ps."JAN", 0) AS "JAN",
    COALESCE(ps."FEB", 0) AS "FEB",
    COALESCE(ps."MAR", 0) AS "MAR",
    COALESCE(ps."APR", 0) AS "APR",
    COALESCE(ps."MAY", 0) AS "MAY",
    COALESCE(ps."JUN", 0) AS "JUN",
    COALESCE(ps."JUL", 0) AS "JUL",
    COALESCE(ps."AUG", 0) AS "AUG",
    COALESCE(ps."SEP", 0) AS "SEP",
    COALESCE(ps."OCT", 0) AS "OCT",
    COALESCE(ps."NOV", 0) AS "NOV",
    COALESCE(ps."DEC", 0) AS "DEC",
    COALESCE(ps."TOTAL", 0) AS "TOTAL"
FROM
    res_partner AS rp
    
-- --- ADDED JOIN 1: Connect Partner to Area Master ---
LEFT JOIN
    area_master AS area ON rp.area_id = area.id

-- --- ADDED JOIN 2: Connect Area Master to CRM Team (Route) ---
LEFT JOIN
    crm_team AS ct ON area.route_id = ct.id

LEFT JOIN
    PivotedSales AS ps ON rp.id = ps.partner_id
WHERE
    -- Only show customers who actually had sales
    COALESCE(ps."TOTAL", 0) > 0
ORDER BY
    "ROUTE";
    """
