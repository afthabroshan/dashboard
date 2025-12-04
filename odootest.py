import streamlit as st
import pandas as pd
import psycopg2

# --- Database Connection ---

# WARNING: Hardcoding credentials is insecure. Use secrets management for production.
DB_HOST = "localhost"  # Replace with your actual host
DB_PORT = "5432"             # Replace with your actual port
DB_NAME = "Kosko_staging" # Replace with your actual database name
DB_USER =  "postgres"# Replace with your actual username
DB_PASS = "12345" # Replace with your actual password

from queries.daily_sales_report import (
    Daily_Sales_report_DXB,
    Daily_Sales_report_Jed,
    Daily_Sales_report_Dmm,
    Daily_Sales_report_Ryd,
    Daily_Sales_report_AXA
)
from queries.customer_report import (
    monthly_sales_report_MSCT,
    monthly_sales_report_Salalah,
    monthly_sales_report_Bahrain,
    monthly_sales_report_JED,
    monthly_sales_report_AXA,
    monthly_sales_report_RUH,
    monthly_sales_report_DMM,
)

from queries.total_sales_report import (
    total_sales_report_Oman,
)

from queries.own_brand_stock import (
    obs,
)

from queries.sales_man_monthly import (
    sales_man_monthly_DXB,
    sales_man_monthly_APEX,
    sales_man_monthly_Main_land,
    sales_man_monthly_Muscut,
    sales_man_monthly_Bahrine,
    sales_man_monthly_Jeddah,
    sales_man_monthly_dammam,
    sales_man_monthly_riyadh,
    sales_man_monthly_axa,
    sales_man_monthly_salah,
)

from queries.sales_man_daily import (
    sales_man_daily_UAE,
    sales_man_daily_APEX,
    sales_man_daily_Main_Land,
    sales_man_daily_Muscat,
    sales_man_daily_Bahrine,
    sales_man_daily_Jeddah,
    sales_man_daily_Dammam,
    sales_man_daily_Riyadh,
    sales_man_daily_AXA,
    sales_man_daily_Salah,
)
# Use st.cache_resource to only create the connection once
# @st.cache_resource
def init_connection():
    try:
        return psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return None

conn = init_connection()

# --- Data Fetching ---

# Function to run query and fetch data as DataFrame, cached for performance
# @st.cache_data
def run_query_df(query):
    # Ensure the connection object isn't stale if cached resource needs re-run
    # For this simple app, it's less likely, but good practice if connection might expire.
    # We can rely on st.cache_resource to manage the connection object lifecycle here.
    if conn:
        try:
            return pd.read_sql_query(query, conn)
        except Exception as e: # Catch pandas or psycopg2 errors
            st.error(f"Error executing query or creating DataFrame: {e}")
            return pd.DataFrame() # Return empty DataFrame on error
    return pd.DataFrame()

# --- Streamlit App ---

st.set_page_config(layout="wide") # Use the full page width
st.title("Enterprise Dashboard")

if st.button("Go to Executive Dashboard"):
    st.switch_page("pages/Dashboard.py")



sales_man_report = """
SELECT
    -- Changed this column to only show Salesman
    COALESCE(rp.name, 'Unassigned Salesman') AS "SALES MAN",
    
    -- All SUMs remain the same
    SUM(m."TOTAL INV AMT") AS "TOTAL INV AMT",
    SUM(m."RETURN BILL AMT") AS "RETURN BILL AMT",
    (SUM(m."TOTAL INV AMT") - SUM(m."RETURN BILL AMT")) AS "CURRENT INV AMOUNT",
    SUM(m."SECURITY CHQ") AS "SECURITY CHQ",
    SUM(m."CHEQUE") AS "CHEQUE",
    SUM(m."CASH") AS "CASH"
FROM (
    -- ---- Block 1: Invoices/Returns ----
    SELECT
        am.invoice_user_id AS user_id,
        am.area_id,
        SUM(CASE WHEN am.move_type = 'out_invoice' THEN am.amount_total ELSE 0 END) AS "TOTAL INV AMT",
        SUM(CASE WHEN am.move_type = 'out_refund' THEN am.amount_total ELSE 0 END) AS "RETURN BILL AMT",
        0 AS "CASH",
        0 AS "CHEQUE",
        0 AS "SECURITY CHQ"
    FROM
        account_move AS am
    WHERE
        am.move_type IN ('out_invoice', 'out_refund')
        -- !!! ADD YOUR DATE FILTER HERE
        -- AND am.invoice_date BETWEEN '2025-01-01' AND '2025-01-31'
    GROUP BY
        am.invoice_user_id, am.area_id
 
    UNION ALL
 
    -- ---- Block 2: Cash/Cheque Payments ----
    SELECT
        ap.user_id,
        p.area_id,
        0 AS "TOTAL INV AMT",
        0 AS "RETURN BILL AMT",
        SUM(CASE WHEN aj.type = 'cash' THEN ap.amount ELSE 0 END) AS "CASH",
        SUM(CASE WHEN aj.type = 'bank' THEN ap.amount ELSE 0 END) AS "CHEQUE",
        0 AS "SECURITY CHQ"
    FROM
        account_payment AS ap
    JOIN
        account_payment_method_line AS apml ON ap.payment_method_line_id = apml.id
    JOIN
        account_journal AS aj ON apml.journal_id = aj.id
    JOIN
        res_partner AS p ON ap.partner_id = p.id
    WHERE
        ap.payment_type = 'inbound' -- Customer Payments
        -- !!! ADD YOUR DATE FILTER HERE
        -- AND ap.date BETWEEN '2025-01-01' AND '2025-01-31'
    GROUP BY
        ap.user_id, p.area_id
 
    UNION ALL
 
    -- ---- Block 3: Security Cheques (PDC) ----
    SELECT
        CAST(NULL AS INTEGER) AS user_id,
        p.area_id,
        0 AS "TOTAL INV AMT",
        0 AS "RETURN BILL AMT",
        0 AS "CASH",
        0 AS "CHEQUE",
        SUM(pdc.amount) AS "SECURITY CHQ"
    FROM
        pdc_payment AS pdc
    JOIN
        res_partner AS p ON pdc.partner_id = p.id
     WHERE
    --    pdc.state = 'posted' -- Assuming 'posted' or similar
        -- !!! ADD YOUR DATE FILTER HERE
          pdc.due_date BETWEEN '2025-05-01' AND '2025-08-1'
    GROUP BY
        p.area_id
) AS m
LEFT JOIN
    res_users AS ru ON m.user_id = ru.id
LEFT JOIN
    res_partner AS rp ON ru.partner_id = rp.id
LEFT JOIN
    area_master AS am ON m.area_id = am.id
GROUP BY
    rp.name -- Changed: Group only by Salesman
ORDER BY
    rp.name NULLS FIRST; -- Changed: Sort only by Salesman
"""



def display_data_tab(query, tab_name):
    """Helper function to display data in a tab."""
    st.subheader(f"Data for {tab_name}")
    df = run_query_df(query)
    if not df.empty:
        st.dataframe(df, use_container_width=True)
        st.write(f"Total rows: {len(df)}")
    else:
        if conn:
            st.info("No data found.")

# --- Layout Structure ---

# 1. Sales Section
st.header("Daily Sales Report")
sales_tabs = st.tabs(["DXB", "JED", "DMM", "RYD", "AXA"])

with sales_tabs[0]:
    display_data_tab(Daily_Sales_report_DXB, "DXB")

with sales_tabs[1]:
    display_data_tab(Daily_Sales_report_Jed, "JED")

with sales_tabs[2]:
    display_data_tab(Daily_Sales_report_Dmm, "DMM")

with sales_tabs[3]:
    display_data_tab(Daily_Sales_report_Ryd, "RYD")

with sales_tabs[4]:
    display_data_tab(Daily_Sales_report_AXA, "AXA")

st.markdown("---") # Separator

# 2. Products Section
st.header("Monthly Sales")
product_tabs = st.tabs(["MSCT", "Salalah", "Bahrain", "JED", "AXA", "RUH", "DMM"])

with product_tabs[0]:
    display_data_tab(monthly_sales_report_MSCT, "MSCT")

with product_tabs[1]:
    display_data_tab(monthly_sales_report_Salalah, "Salalah")

with product_tabs[2]:
    display_data_tab(monthly_sales_report_Bahrain, "Bahrain")

with product_tabs[3]:
    display_data_tab(monthly_sales_report_JED, "JED")

with product_tabs[4]:
    display_data_tab(monthly_sales_report_AXA, "AXA")

with product_tabs[5]:
    display_data_tab(monthly_sales_report_RUH, "RUH")

with product_tabs[6]:
    display_data_tab(monthly_sales_report_DMM, "DMM")

st.markdown("---") # Separator

# 3. Sales man Section
st.header("Total Sales Report")
dummy_tabs = st.tabs([ "Oman","UAE", "Saudi"])

with dummy_tabs[0]:
    display_data_tab(total_sales_report_Oman, "Oman")

with dummy_tabs[1]:
    display_data_tab(total_sales_report_Oman, "UAE")

with dummy_tabs[2]:
    display_data_tab(total_sales_report_Oman, "Saudi")

st.markdown("---") # Separator

# 4. Own Brand Stock
st.header("Own Brand Stock")
display_data_tab(obs, "Own Brand Stock")

#4. Sales_man Montly
st.markdown("---") # Separator
st.header("Sales_man Monthly Report")
dummy_tabs = st.tabs([ "UAE","Jafza", "Main Land", "Muscat", "Bahrain", "Jeddah", "Dammam", "Riyadh", "AXA", "Salalah"])


with dummy_tabs[0]:
    display_data_tab(sales_man_monthly_DXB, "UAE")

with dummy_tabs[1]:
    display_data_tab(sales_man_monthly_APEX, "Jafza")

with dummy_tabs[2]:
    display_data_tab(sales_man_monthly_Main_land, "Main Land")

with dummy_tabs[3]:
    display_data_tab(sales_man_monthly_Muscut, "Muscat")

with dummy_tabs[4]:
    display_data_tab(sales_man_monthly_Bahrine, "Bahrain")

with dummy_tabs[5]:
    display_data_tab(sales_man_monthly_Jeddah, "Jeddah")

with dummy_tabs[6]:
    display_data_tab(sales_man_monthly_dammam, "Dammam")

with dummy_tabs[7]:
    display_data_tab(sales_man_monthly_riyadh, "Riyadh")

with dummy_tabs[8]:
    display_data_tab(sales_man_monthly_axa, "AXA")

with dummy_tabs[9]:
    display_data_tab(sales_man_monthly_salah, "Salalah")



    #4. Sales_man Daily
st.markdown("---") # Separator
st.header("Sales_man Daily Report")
dummy_tabs = st.tabs([ "UAE","Jafza", "Main Land", "Muscat", "Bahrain", "Jeddah", "Dammam", "Riyadh", "AXA", "Salalah"])


with dummy_tabs[0]:
    display_data_tab(sales_man_daily_UAE, "UAE")

with dummy_tabs[1]:
    display_data_tab(sales_man_daily_APEX, "Jafza")

with dummy_tabs[2]:
    display_data_tab(sales_man_daily_Main_Land, "Main Land")

with dummy_tabs[3]:
    display_data_tab(sales_man_daily_Muscat, "Muscat")

with dummy_tabs[4]:
    display_data_tab(sales_man_daily_Bahrine, "Bahrain")

with dummy_tabs[5]:
    display_data_tab(sales_man_daily_Jeddah, "Jeddah")

with dummy_tabs[6]:
    display_data_tab(sales_man_daily_Dammam, "Dammam")

with dummy_tabs[7]:
    display_data_tab(sales_man_daily_Riyadh, "Riyadh")

with dummy_tabs[8]:
    display_data_tab(sales_man_daily_AXA, "AXA")

with dummy_tabs[9]:
    display_data_tab(sales_man_daily_Salah, "Salalah")