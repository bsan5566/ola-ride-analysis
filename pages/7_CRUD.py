import streamlit as st
import pandas as pd
import mysql.connector
from Database.db import get_connection  # using your existing db.py

st.set_page_config(page_title="CRUD Operations", layout="wide")
st.title("🛠 CRUD Operations - OLA Ride Data")

# --- Helper function ---
def run_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or ())
    if query.strip().lower().startswith("select"):
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    else:
        conn.commit()
        cursor.close()
        conn.close()

# --- Tabs for CRUD ---
tabs = st.tabs(["➕ Create", "📖 Read", "✏️ Update", "❌ Delete"])

# --- CREATE ---
with tabs[0]:
    st.subheader("Add New Ride Record")
    with st.form("create_form"):
        booking_id = st.text_input("Booking ID")
        customer_id = st.text_input("Customer ID")
        vehicle_type = st.selectbox("Vehicle Type", ["Auto", "Mini", "Prime Sedan", "Bike", "eBike", "Prime Plus"])
        booking_status = st.selectbox("Booking Status", ["Success", "Canceled by Customer", "Canceled by Driver", "Driver Not Found"])
        booking_value = st.number_input("Booking Value", min_value=0.0, step=0.1)
        payment_method = st.selectbox("Payment Method", ["Cash", "UPI", "Credit Card", "Debit Card"])
        ride_distance = st.number_input("Ride Distance", min_value=0.0, step=0.1)
        driver_ratings = st.number_input("Driver Ratings", min_value=0.0, max_value=5.0, step=0.1)
        customer_rating = st.number_input("Customer Ratings", min_value=0.0, max_value=5.0, step=0.1)
        submit = st.form_submit_button("Add Record")
    
    if submit:
        run_query(
            """INSERT INTO OLA_Data 
            (Booking_ID, Customer_ID, Vehicle_Type, Booking_Status, Booking_Value, Payment_Method, Ride_Distance, Driver_Ratings, Customer_Rating)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (booking_id, customer_id, vehicle_type, booking_status, booking_value, payment_method, ride_distance, driver_ratings, customer_rating)
        )
        st.success("✅ Record added successfully!")

# --- READ ---
with tabs[1]:
    st.subheader("View Records")
    rows = run_query("SELECT * FROM OLA_Data LIMIT 50")
    df = pd.DataFrame(rows)
    st.dataframe(df)

# --- UPDATE ---
with tabs[2]:
    st.subheader("Update Ride Record")
    ids = run_query("SELECT Booking_ID FROM OLA_Data LIMIT 100")
    id_list = [r["Booking_ID"] for r in ids]
    selected_id = st.selectbox("Select Booking ID", id_list)
    new_status = st.selectbox("New Booking Status", ["Success", "Canceled by Customer", "Canceled by Driver", "Driver Not Found"])
    new_rating = st.number_input("New Driver Rating", min_value=0.0, max_value=5.0, step=0.1)
    if st.button("Update Record"):
        run_query(
            "UPDATE OLA_Data SET Booking_Status=%s, Driver_Ratings=%s WHERE Booking_ID=%s",
            (new_status, new_rating, selected_id)
        )
        st.success("✅ Record updated successfully!")

# --- DELETE ---
with tabs[3]:
    st.subheader("Delete Ride Record")

    delete_id = st.text_input("Enter Booking ID to Delete")

    if st.button("Delete Record"):
        if delete_id.strip() != "":
            try:
                run_query("DELETE FROM ola_data WHERE Booking_ID=%s", (delete_id,))
                st.warning(f"⚠️ Record with Booking_ID={delete_id} deleted (if it existed).")
            except Exception as e:
                st.error(f"⚠️ Could not delete data: {e}")
        else:
            st.error("❌ Please enter a valid Booking ID.")

