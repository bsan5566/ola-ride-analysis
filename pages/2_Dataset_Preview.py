# pages/2_Dataset_Preview.py
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dataset Preview", layout="wide")
st.title("📂 OLA Dataset Preview")

# ============================
# File Paths (relative to repo)
# ============================
dataset_dir = "Dataset"
xlsx_file = "OLA_Dataset.xlsx"
csv_file = "OLA_DataSet_Cleaned.csv"

xlsx_path = os.path.join("Dataset", "OLA_DataSet.xlsx")
csv_path = os.path.join(dataset_dir, csv_file)

# ============================
# 1️⃣ Raw Excel Dataset
# ============================
st.subheader("1️⃣ Raw Dataset (Excel)")
if os.path.exists(xlsx_path):
    try:
        df_xlsx = pd.read_excel(xlsx_path, sheet_name=0)
        st.success(f"✅ Successfully loaded **{xlsx_file}**")
        st.dataframe(df_xlsx.head(50), use_container_width=True)
        with open(xlsx_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Raw Dataset (Excel)",
                data=f,
                file_name=xlsx_file,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    except Exception as e:
        st.error(f"❌ Error loading Excel file: {e}")
else:
    st.error(f"⚠️ Raw dataset file not found at path: {xlsx_path}")

# ============================
# 2️⃣ Cleaned CSV Dataset
# ============================
st.subheader("2️⃣ Cleaned Dataset (CSV)")
if os.path.exists(csv_path):
    try:
        df_csv = pd.read_csv(csv_path)
        st.success(f"✅ Successfully loaded **{csv_file}**")
        st.dataframe(df_csv.head(50), use_container_width=True)
        with open(csv_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Cleaned Dataset (CSV)",
                data=f,
                file_name=csv_file,
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"❌ Error loading CSV file: {e}")
else:
    st.error(f"⚠️ Cleaned dataset file not found at path: {csv_path}")
