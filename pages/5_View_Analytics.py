# pages/2_Analytics.py
import streamlit as st
import plotly.express as px
from Database.db import run_query
from streamlit_option_menu import option_menu
import os

# ============================
# Streamlit Config
# ============================
st.set_page_config(page_title="OLA Ride View Analytics", layout="wide")

st.title("📊 OLA Ride View Analytics Dashboard")

# ============================
# Navbar (Top Menu)
# ============================
selected = option_menu(
    menu_title=None,  # No title
    options=["Overall", "Vehicle Type", "Revenue", "Cancellation", "Ratings", "View Power BI Report","Queries for view analytics"],
    icons=["bar-chart", "car-front", "currency-exchange", "x-circle", "star", "download","list-task"],
    default_index=0,
    orientation="horizontal",
)

# ============================
# 1. OVERALL
# ============================
if selected == "Overall":
    st.subheader("📈 Ride Volume Over Time")
    df, msg = run_query("""
        SELECT Date, COUNT(*) AS Total_Rides 
        FROM OLA_Data GROUP BY Date ORDER BY Date;
    """)
    if df is None or df.empty:
        st.warning("No ride volume data available.")
    else:
        fig = px.line(df, x="Date", y="Total_Rides", title="Ride Volume Over Time")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df)

    st.subheader("📌 Booking Status Breakdown")
    df2, msg = run_query("""
        SELECT Booking_Status, COUNT(*) AS Total_Bookings
        FROM OLA_Data GROUP BY Booking_Status;
    """)
    if df2 is None or df2.empty:
        st.warning("No booking status data available.")
    else:
        fig2 = px.pie(df2, names="Booking_Status", values="Total_Bookings",
                      title="Booking Status Breakdown")
        st.plotly_chart(fig2, use_container_width=True)
        st.dataframe(df2)

# ============================
# 2. VEHICLE TYPE
# ============================
elif selected == "Vehicle Type":
    st.subheader("🚗 Top 5 Vehicle Types by Ride Distance")
    df, msg = run_query("""
        SELECT Vehicle_Type, SUM(Ride_Distance) AS Total_Distance
        FROM OLA_Data GROUP BY Vehicle_Type
        ORDER BY Total_Distance DESC LIMIT 5;
    """)
    if df is None or df.empty:
        st.warning("No vehicle type data available.")
    else:
        fig = px.bar(df, x="Total_Distance", y="Vehicle_Type", orientation="h",
                     title="Top 5 Vehicle Types by Ride Distance")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df)

# ============================
# 3. REVENUE
# ============================
elif selected == "Revenue":
    st.subheader("💰 Revenue by Payment Method")
    df, msg = run_query("""
        SELECT Payment_Method, SUM(Booking_Value) AS Total_Revenue
        FROM OLA_Data WHERE Booking_Status='Success'
        GROUP BY Payment_Method;
    """)
    if df is None or df.empty:
        st.warning("No revenue data available.")
    else:
        fig = px.bar(df, x="Payment_Method", y="Total_Revenue",
                     title="Revenue by Payment Method")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df)

    st.subheader("🏆 Top 5 Customers by Spending")
    df2, msg = run_query("""
        SELECT Customer_ID, SUM(Booking_Value) AS Total_Spending
        FROM OLA_Data WHERE Booking_Status='Success'
        GROUP BY Customer_ID ORDER BY Total_Spending DESC LIMIT 5;
    """)
    if df2 is None or df2.empty:
        st.warning("No customer spending data available.")
    else:
        fig2 = px.bar(df2, x="Total_Spending", y="Customer_ID", orientation="h",
                      title="Top 5 Customers by Spending")
        st.plotly_chart(fig2, use_container_width=True)
        st.dataframe(df2)

    st.subheader("📊 Ride Distance Per Day")
    df3, msg = run_query("""
        SELECT Date, SUM(Ride_Distance) AS Total_Distance
        FROM OLA_Data GROUP BY Date ORDER BY Date;
    """)
    if df3 is None or df3.empty:
        st.warning("No ride distance data available.")
    else:
        fig3 = px.area(df3, x="Date", y="Total_Distance",
                       title="Ride Distance Distribution Per Day")
        st.plotly_chart(fig3, use_container_width=True)
        st.dataframe(df3)

# ============================
# 4. CANCELLATION
# ============================
elif selected == "Cancellation":
    st.subheader("❌ Customer Cancellation Reasons")
    df, msg = run_query("""
        SELECT Incomplete_Rides_Reason, COUNT(*) AS Total_Customer_Cancellations
        FROM OLA_Data WHERE Booking_Status='Canceled by Customer'
        GROUP BY Incomplete_Rides_Reason;
    """)
    if df is None or df.empty:
        st.warning("No customer cancellations found.")
    else:
        fig = px.bar(df, x="Total_Customer_Cancellations", y="Incomplete_Rides_Reason",
                     orientation="h", title="Customer Cancellation Reasons")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df)

    st.subheader("🚫 Driver Cancellation Reasons")
    df2, msg = run_query("""
        SELECT Incomplete_Rides_Reason, COUNT(*) AS Total_Driver_Cancellations
        FROM OLA_Data WHERE Booking_Status='Canceled by Driver'
        GROUP BY Incomplete_Rides_Reason;
    """)
    if df2 is None or df2.empty:
        st.warning("No driver cancellations found.")
    else:
        fig2 = px.bar(df2, x="Total_Driver_Cancellations", y="Incomplete_Rides_Reason",
                      orientation="h", title="Driver Cancellation Reasons")
        st.plotly_chart(fig2, use_container_width=True)
        st.dataframe(df2)

# ============================
# 5. RATINGS
# ============================
elif selected == "Ratings":
    st.subheader("⭐ Average Driver Ratings by Vehicle Type")
    df, msg = run_query("""
        SELECT Vehicle_Type, AVG(Driver_Ratings) AS Avg_Driver_Rating
        FROM OLA_Data WHERE Driver_Ratings IS NOT NULL
        GROUP BY Vehicle_Type;
    """)
    if df is None or df.empty:
        st.warning("No driver ratings found.")
    else:
        fig = px.bar(df, x="Vehicle_Type", y="Avg_Driver_Rating",
                     title="Average Driver Ratings by Vehicle Type")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df)

    st.subheader("⭐ Average Customer Ratings by Vehicle Type")
    df2, msg = run_query("""
        SELECT Vehicle_Type, AVG(Customer_Rating) AS Avg_Customer_Rating
        FROM OLA_Data WHERE Customer_Rating IS NOT NULL
        GROUP BY Vehicle_Type;
    """)
    if df2 is None or df2.empty:
        st.warning("No customer ratings found.")
    else:
        fig2 = px.bar(df2, x="Vehicle_Type", y="Avg_Customer_Rating",
                      title="Average Customer Ratings by Vehicle Type")
        st.plotly_chart(fig2, use_container_width=True)
        st.dataframe(df2)

# ============================
# 6. POWER BI REPORT
# ============================
elif selected == "View Power BI Report":
    st.subheader("📥 Download OLA RIDE VIEW Report")

    pbix_path = "C:/Users/B santosh/Downloads/ola/Ola_ride_/PowerBi_Files/ola_ride_views.pbix"  

    if os.path.exists(pbix_path):
        with open(pbix_path, "rb") as f:
            st.download_button(
                label="⬇️ Download OLA Ride View Insights.pbix",
                data=f,
                file_name="OLA_Ride_View_Insights.pbix",
                mime="application/octet-stream"
            )
    else:
        st.error("⚠️ Power BI file not found. Please check the file path.")
# ============================
# 7. Queries for view analytics 
# ============================
elif selected == "Queries for view analytics":
    st.subheader("📥 Download Queries for view analytics")

    pbix_path = "C:/Users/B santosh/Downloads/ola/Ola_ride_/Sql_query/queries_view_analytics.sql"

    if os.path.exists(pbix_path):
        with open(pbix_path, "rb") as f:
            st.download_button(
                label="⬇️ Download OLA Ride queries_view_analytics.sql",
                data=f,
                file_name="queries_view_analytics.sql",
                mime="application/octet-stream"
            )
    else:
        st.error("⚠️ Power BI file not found. Please check the file path.")