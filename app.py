import streamlit as st

st.set_page_config(page_title="OLA Ride Insights", layout="wide")

# Define all pages
pages = {
    "🏠 Home": st.Page("pages/1_Home.py", title="Home"),
    "🗂 Dataset Preview": st.Page("pages/2_Dataset_Preview.py", title="Dataset Preview"),
    "📥 SQL Queries": st.Page("pages/3_Sql_Queries.py", title="SQL Queries"),
    "📈 Power BI": st.Page("pages/4_PowerBI_Question_analytics.py", title="Power BI Questions"),
    "📊 View Analytics": st.Page("pages/5_View_Analytics.py", title="View Analytics"),
    "📑 EDA Notebook": st.Page("pages/6_EDA_Notebook.py", title="EDA Notebook"),
 }

# Navigation bar
nav = st.navigation(list(pages.values()))

# Run selected page
nav.run()
