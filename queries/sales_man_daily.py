sales_man_daily_UAE="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 1
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""


sales_man_daily_APEX="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 2
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""



sales_man_daily_Main_Land="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 3
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""



sales_man_daily_Muscat="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 4
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""



sales_man_daily_Bahrine="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 5
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""



sales_man_daily_Jeddah="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 6
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""



sales_man_daily_Dammam="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 7
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""



sales_man_daily_Riyadh="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 8
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""



sales_man_daily_AXA="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 9
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""



sales_man_daily_Salah="""
WITH MonthlyData AS (
    SELECT
        rc.name AS branch_name,
        COALESCE(rp_salesman.name, 'Unassigned Salesman') AS salesman_name,
        EXTRACT(DAY FROM am.date) AS day_num,
        ap.amount
    FROM account_payment ap
    JOIN account_move am ON ap.move_id = am.id
    JOIN res_company rc ON am.company_id = rc.id
    JOIN res_partner rp_cust ON ap.partner_id = rp_cust.id
    LEFT JOIN res_users ru ON rp_cust.user_id = ru.id
    LEFT JOIN res_partner rp_salesman ON ru.partner_id = rp_salesman.id
    WHERE 
        -- 1. FILTER: Select Your Branch ID Here (e.g., 1 for Dubai, 4 for Muscat)
        am.company_id = 10
        
        -- 2. FILTER: Select Your Month Here
        AND am.date >= '2025-04-01' AND am.date <= '2025-04-30'
        
        -- 3. Standard Filters (Confirmed Income)
        AND am.state = 'posted'
        AND ap.payment_type = 'inbound'
)

-- Main Query: Salesman Rows
SELECT
    ROW_NUMBER() OVER(ORDER BY salesman_name) AS "SL NO",
    branch_name AS "Branch",
    salesman_name AS "Salesman",
    
    -- Daily Columns (1 to 31)
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END) AS "1",
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END) AS "2",
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END) AS "3",
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END) AS "4",
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END) AS "5",
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END) AS "6",
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END) AS "7",
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END) AS "8",
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END) AS "9",
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END) AS "10",
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END) AS "11",
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END) AS "12",
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END) AS "13",
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END) AS "14",
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END) AS "15",
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END) AS "16",
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END) AS "17",
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END) AS "18",
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END) AS "19",
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END) AS "20",
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END) AS "21",
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END) AS "22",
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END) AS "23",
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END) AS "24",
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END) AS "25",
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END) AS "26",
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END) AS "27",
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END) AS "28",
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END) AS "29",
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END) AS "30",
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END) AS "31",

    -- Salesman Total
    SUM(amount) AS "TOTAL"
FROM MonthlyData
GROUP BY branch_name, salesman_name

UNION ALL

-- Bottom Row: Grand Total
SELECT
    NULL AS "SL NO",
    MAX(branch_name) AS "Branch", -- Keeps the branch name in the total row
    'GRAND TOTAL' AS "Salesman",
    
    -- Daily Totals
    SUM(CASE WHEN day_num = 1 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 2 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 3 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 4 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 5 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 6 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 7 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 8 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 9 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 10 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 11 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 12 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 13 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 14 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 15 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 16 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 17 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 18 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 19 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 20 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 21 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 22 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 23 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 24 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 25 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 26 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 27 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 28 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 29 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 30 THEN amount ELSE 0 END),
    SUM(CASE WHEN day_num = 31 THEN amount ELSE 0 END),

    -- Month Grand Total
    SUM(amount)
FROM MonthlyData

ORDER BY "SL NO" NULLS LAST;
"""