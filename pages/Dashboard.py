import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.title("Executive Dashboard")

# Dummy Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Revenue", value="$1.2M", delta="12%")

with col2:
    st.metric(label="Total Orders", value="3,450", delta="-5%")

with col3:
    st.metric(label="Active Customers", value="1,200", delta="8%")

with col4:
    st.metric(label="Avg. Order Value", value="$350", delta="2%")

st.markdown("---")

# Dummy Charts
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Sales by Region")
    chart_data = pd.DataFrame(
        np.random.rand(5, 3),
        columns=["UAE", "Oman", "Saudi"]
    )
    st.bar_chart(chart_data)

with col_right:
    st.subheader("Monthly Growth Trend")
    trend_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["UAE", "Oman", "Saudi"]
    )
    st.line_chart(trend_data)

st.markdown("---")
st.subheader("Recent Transactions")
df_dummy = pd.DataFrame({
    "Order ID": [f"ORD-{i}" for i in range(1001, 1006)],
    "Customer": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Amount": [120, 450, 320, 150, 800],
    "Status": ["Completed", "Pending", "Completed", "Shipped", "Processing"]
})
st.dataframe(df_dummy, use_container_width=True)
