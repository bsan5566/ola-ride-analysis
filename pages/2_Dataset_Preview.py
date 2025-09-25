import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dataset Preview", layout="wide")
st.title("📂 OLA Dataset Preview")

# ============================
# File Paths (adjust as needed)
# ============================
xlsx_path = os.path.join("Dataset", "OLA_Dataset.xlsx")
csv_path = os.path.join("Dataset", "OLA_DataSet_Cleaned.csv")

# ============================
# Load & Display Excel
# ============================
st.subheader("1️⃣ Raw Dataset (Excel)")
if os.path.exists(xlsx_path):
    try:
        df_xlsx = pd.read_excel(xlsx_path, sheet_name=0)
        st.write("✅ Successfully loaded **OLA_Dataset.xlsx**")
        st.dataframe(df_xlsx.head(50), use_container_width=True)
        st.download_button(
            label="⬇️ Download Raw Dataset (Excel)",
            data=open(xlsx_path, "rb").read(),
            file_name="OLA_Dataset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"❌ Error loading Excel file: {e}")
else:
    st.error("⚠️ Raw dataset file not found. Please check the path.")

# ============================
# Load & Display CSV
# ============================
st.subheader("2️⃣ Cleaned Dataset (CSV)")
if os.path.exists(csv_path):
    try:
        df_csv = pd.read_csv(csv_path)
        st.write("✅ Successfully loaded **OLA_DataSet_Cleaned.csv**")
        st.dataframe(df_csv.head(50), use_container_width=True)
        st.download_button(
            label="⬇️ Download Cleaned Dataset (CSV)",
            data=open(csv_path, "rb").read(),
            file_name="OLA_DataSet_Cleaned.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"❌ Error loading CSV file: {e}")
else:
    st.error("⚠️ Cleaned dataset file not found. Please check the path.")
