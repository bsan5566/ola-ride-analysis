import streamlit as st
import mysql.connector

# Function to get a database connection using Streamlit secrets
import mysql.connector
import streamlit as st

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        port=st.secrets["mysql"]["port"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

import pandas as pd

def run_query(query):
    try:
        conn = get_connection()
        df = pd.read_sql(query, conn)   # return results as DataFrame
        conn.close()
        return df, "Query executed successfully!"
    except Exception as e:
        return None, f"Error: {e}"
