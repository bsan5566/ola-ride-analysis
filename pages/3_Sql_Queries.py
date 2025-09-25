# pages/3_SQL_Queries.py
import streamlit as st
from Database.db import run_query  
import os
# ============================
# Streamlit UI
# ============================
st.set_page_config(page_title="SQL Query Runner", layout="wide")
st.title("📝 OLA RIDE SQL INSIGHTS")

# Download SQL_queries File
# ============================
st.markdown("---")
st.subheader("📥 Download Sql Queries  Report")

sql_query = os.path.join("Sql_query", "queries.sql")  

if os.path.exists(sql_query):
    with open(sql_query, "rb") as f:
        st.download_button(
            label="⬇️ Download queries.sql",
            data=f,
            file_name="queries.sql",
            mime="application/octet-stream"
        )
else:
    st.error("⚠️ Power BI file not found. Please check the path.")


st.markdown("Select a query from the dropdown below and click **Run Query** to view results.")

# Predefined queries (friendly name → SQL query)
queries = {
    "View the data in the OLA_Data table":
        "SELECT * FROM OLA_Data;",
    "All Successful Bookings":
        "SELECT * FROM OLA_Data WHERE Booking_Status = 'Success';",

    "Average Ride Distance per Vehicle Type":
        "SELECT Vehicle_Type, AVG(Ride_Distance) AS Avg_Distance FROM OLA_Data GROUP BY Vehicle_Type;",

    "Total Cancelled Rides by Customers":
        "SELECT COUNT(*) AS Total_Customer_Cancellations FROM OLA_Data WHERE Booking_Status = 'Canceled by Customer';",

    "Top 5 Customers by Rides":
        "SELECT Customer_ID, COUNT(*) AS Total_Rides FROM OLA_Data GROUP BY Customer_ID ORDER BY Total_Rides DESC LIMIT 5;",

    "Driver Cancellations (Personal/Car Issues)":
        "SELECT Incomplete_Rides_Reason, COUNT(*) AS Total_Driver_Cancellations "
        "FROM OLA_Data WHERE Booking_Status = 'Canceled by Driver' "
        "AND Incomplete_Rides_Reason IN ('Personal','Car Issue') "
        "GROUP BY Incomplete_Rides_Reason;",

    "Max/Min Driver Ratings for Prime Sedan":
        "SELECT MAX(Driver_Ratings) AS Max_Rating, MIN(Driver_Ratings) AS Min_Rating "
        "FROM OLA_Data WHERE Vehicle_Type = 'Prime Sedan';",

    "Rides with UPI Payments":
        "SELECT * FROM OLA_Data WHERE Payment_Method = 'UPI';",

    "Average Customer Rating per Vehicle Type":
        "SELECT Vehicle_Type, AVG(Customer_Rating) AS Avg_Customer_Rating "
        "FROM OLA_Data GROUP BY Vehicle_Type;",

    "Total Revenue from Successful Rides":
        "SELECT SUM(Booking_Value) AS Total_Successful_Revenue "
        "FROM OLA_Data WHERE Booking_Status = 'Success';",

    "All Incomplete Rides with Reasons":
        "SELECT Booking_ID, Customer_ID, Vehicle_Type, Incomplete_Rides, Incomplete_Rides_Reason "
        "FROM OLA_Data WHERE Incomplete_Rides = 'Yes';"
}


# Dropdown for query selection
selected_query = st.selectbox("📌 Choose a query to run", list(queries.keys()))

# Run button
if st.button("▶️ Run Query"):
    query_to_run = queries[selected_query]
    df, msg = run_query(query_to_run)

    st.info(msg)
    if df is not None and not df.empty:
        st.dataframe(df, use_container_width=True)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Results as CSV", data=csv, file_name="query_results.csv", mime="text/csv")

