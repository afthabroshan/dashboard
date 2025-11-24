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
st.title("Sales Order Lines")

# Define the SQL query
sql_query = """
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
        and so.company_id = 1
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

# Fetch data into a Pandas DataFrame
df_sales = run_query_df(sql_query)

if not df_sales.empty:
    st.write("Displaying Daily Sales Report (using Order Totals)")

    # Display the DataFrame as a table
    st.dataframe(df_sales, use_container_width=True) # Makes the table use full width

    st.write(f"Total days with sales: {len(df_sales)-1}")
else:
     if conn: # Only show this if the connection was successful but no data was returned
        st.write("No sales data found for the specified date range.")

# Note: No need to explicitly close the connection when using st.cache_resource