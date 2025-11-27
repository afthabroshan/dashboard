obs = """
SELECT 
    -- 1. Identify Product by Part Number (Merging Duplicates)
    pp.default_code AS part_number,
    -- FIX: Cast JSONB to TEXT so MAX() can handle it
    MAX(pt.name::text) AS product_name, 

    -- 2. Total In (Purchases + Opening Stock + Returns)
    COALESCE(SUM(moves_in.total_in), 0) AS total_quantity_in,

    -- 3. Total Sales / Out
    COALESCE(SUM(moves_out.total_out), 0) AS total_quantity_sold,

    -- 4. Current Stock Aggregated by Branch (Summing duplicates)
    SUM(COALESCE(pp.mtr_ryd_stcok, 0) + COALESCE(pp.mtr_jed_stcok, 0) + COALESCE(pp.mtr_dammam_stock, 0)) AS mtr_stock,
    SUM(COALESCE(pp.sbc_baharain_stock, 0)) AS bahrain_stock,
    SUM(COALESCE(pp.aft_oman_stock, 0)) AS oman_stock,
    SUM(COALESCE(pp.apex_main_land_stcok, 0)) AS apex_main_land_stock,
    SUM(COALESCE(pp.apex_jafza_stock, 0)) AS apex_jafza_stock,

    -- 5. Real Calculated Balance (Total In - Total Out)
    (COALESCE(SUM(moves_in.total_in), 0) - COALESCE(SUM(moves_out.total_out), 0)) AS calculated_system_balance

FROM product_product pp
JOIN product_template pt ON pp.product_tmpl_id = pt.id

-- Subquery for Incoming Stock (Purchases + Inventory Adjustments)
LEFT JOIN (
    SELECT product_id, SUM(product_uom_qty) as total_in
    FROM stock_move
    WHERE state = 'done' 
      AND location_dest_id IN (SELECT id FROM stock_location WHERE usage = 'internal')
      AND location_id NOT IN (SELECT id FROM stock_location WHERE usage = 'internal')
    GROUP BY product_id
) moves_in ON moves_in.product_id = pp.id

-- Subquery for Outgoing Stock (Sales)
LEFT JOIN (
    SELECT product_id, SUM(product_uom_qty) as total_out
    FROM stock_move
    WHERE state = 'done'
      AND location_id IN (SELECT id FROM stock_location WHERE usage = 'internal')
      AND location_dest_id NOT IN (SELECT id FROM stock_location WHERE usage = 'internal')
    GROUP BY product_id
) moves_out ON moves_out.product_id = pp.id

WHERE 
    pt.active = true
    AND pp.default_code IS NOT NULL -- Exclude products with no Part Number

GROUP BY 
    pp.default_code

ORDER BY 
    pp.default_code;
"""