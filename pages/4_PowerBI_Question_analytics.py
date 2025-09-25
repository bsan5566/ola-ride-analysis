import streamlit as st
import plotly.express as px
from Database.db import run_query
import os

st.set_page_config(page_title="Power BI Questions", layout="wide")
st.title("📊 Power BI Analysis Questions (Visualized)")

# Download Power BI File
# ============================
st.markdown("---")
st.subheader("📥 Download Power BI Report")

pbix_path =  os.path.join("PowerBi_Files", "ola.pbix")  

if os.path.exists(pbix_path):
    with open(pbix_path, "rb") as f:
        st.download_button(
            label="⬇️ Download OLA.pbix",
            data=f,
            file_name="ola.pbix",
            mime="application/octet-stream"
        )
else:
    st.error("⚠️ Power BI file not found. Please check the path.")

# ============================
# 1. Ride Volume Over Time
# ============================
st.subheader("1️⃣ Ride Volume Over Time")
df, msg = run_query("""
    SELECT Date, COUNT(*) AS Total_Rides 
    FROM OLA_Data GROUP BY Date ORDER BY Date;
""")
if df is not None and not df.empty:
    fig = px.line(df, x="Date", y="Total_Rides", title="Ride Volume Over Time")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No data available for Ride Volume Over Time.")

# ============================
# 2. Booking Status Breakdown
# ============================
st.subheader("2️⃣ Booking Status Breakdown")
df, msg = run_query("""
    SELECT Booking_Status, COUNT(*) AS Total_Bookings
    FROM OLA_Data GROUP BY Booking_Status;
""")
if df is not None and not df.empty:
    fig = px.pie(df, names="Booking_Status", values="Total_Bookings", title="Booking Status Breakdown")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No data available for Booking Status Breakdown.")

# ============================
# 3. Top 5 Vehicle Types by Ride Distance
# ============================
st.subheader("3️⃣ Top 5 Vehicle Types by Ride Distance")
df, msg = run_query("""
    SELECT Vehicle_Type, SUM(Ride_Distance) AS Total_Distance
    FROM OLA_Data GROUP BY Vehicle_Type
    ORDER BY Total_Distance DESC LIMIT 5;
""")
if df is not None and not df.empty:
    fig = px.bar(df, x="Total_Distance", y="Vehicle_Type", orientation="h",
                 title="Top 5 Vehicle Types by Ride Distance")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No data available for Vehicle Types.")

# ============================
# 4. Average Customer Ratings by Vehicle Type
# ============================
st.subheader("4️⃣ Average Customer Ratings by Vehicle Type")
df, msg = run_query("""
    SELECT Vehicle_Type, AVG(Customer_Rating) AS Avg_Customer_Rating
    FROM OLA_Data WHERE Customer_Rating IS NOT NULL
    GROUP BY Vehicle_Type;
""")
if df is not None and not df.empty:
    fig = px.bar(df, x="Vehicle_Type", y="Avg_Customer_Rating", title="Average Customer Ratings")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No customer ratings available.")

# ============================
# 5. Canceled Rides Reasons
# ============================
st.subheader("5️⃣ Canceled Rides Reasons")
df, msg = run_query("""
    SELECT Incomplete_Rides_Reason, COUNT(*) AS Total_Cancellations
    FROM OLA_Data WHERE Booking_Status LIKE 'Canceled%'
    GROUP BY Incomplete_Rides_Reason;
""")
if df is not None and not df.empty:
    fig = px.bar(df, x="Total_Cancellations", y="Incomplete_Rides_Reason",
                 orientation="h", title="Canceled Rides Reasons")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No cancellation data available.")

# ============================
# 6. Revenue by Payment Method
# ============================
st.subheader("6️⃣ Revenue by Payment Method")
df, msg = run_query("""
    SELECT Payment_Method, SUM(Booking_Value) AS Total_Revenue
    FROM OLA_Data WHERE Booking_Status='Success'
    GROUP BY Payment_Method;
""")
if df is not None and not df.empty:
    fig = px.bar(df, x="Payment_Method", y="Total_Revenue", title="Revenue by Payment Method")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No revenue data available.")

# ============================
# 7. Top 5 Customers by Total Booking Value
# ============================
st.subheader("7️⃣ Top 5 Customers by Total Booking Value")
df, msg = run_query("""
    SELECT Customer_ID, SUM(Booking_Value) AS Total_Spending
    FROM OLA_Data WHERE Booking_Status='Success'
    GROUP BY Customer_ID ORDER BY Total_Spending DESC LIMIT 5;
""")
if df is not None and not df.empty:
    fig = px.bar(df, x="Total_Spending", y="Customer_ID", orientation="h",
                 title="Top 5 Customers by Total Booking Value")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No spending data available.")

# ============================
# 8. Ride Distance Distribution Per Day
# ============================
st.subheader("8️⃣ Ride Distance Distribution Per Day")
df, msg = run_query("""
    SELECT Date, SUM(Ride_Distance) AS Total_Distance
    FROM OLA_Data GROUP BY Date ORDER BY Date;
""")
if df is not None and not df.empty:
    fig = px.area(df, x="Date", y="Total_Distance", title="Ride Distance Distribution Per Day")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No ride distance data available.")

# ============================
# 9. Driver Ratings Distribution
# ============================
st.subheader("9️⃣ Driver Ratings Distribution")
df, msg = run_query("""
    SELECT Driver_Ratings, COUNT(*) AS Count
    FROM OLA_Data WHERE Driver_Ratings IS NOT NULL
    GROUP BY Driver_Ratings ORDER BY Driver_Ratings;
""")
if df is not None and not df.empty:
    fig = px.bar(df, x="Driver_Ratings", y="Count", title="Driver Ratings Distribution")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No driver ratings available.")

# ============================
# 10. Customer vs. Driver Ratings
# ============================
st.subheader("🔟 Customer vs. Driver Ratings")
df, msg = run_query("""
    SELECT Vehicle_Type, AVG(Customer_Rating) AS Avg_Customer_Rating,
           AVG(Driver_Ratings) AS Avg_Driver_Rating
    FROM OLA_Data
    WHERE Customer_Rating IS NOT NULL AND Driver_Ratings IS NOT NULL
    GROUP BY Vehicle_Type;
""")
if df is not None and not df.empty:
    fig = px.bar(df, x="Vehicle_Type", y=["Avg_Customer_Rating", "Avg_Driver_Rating"],
                 barmode="group", title="Customer vs Driver Ratings")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)
else:
    st.warning("No ratings comparison available.")



