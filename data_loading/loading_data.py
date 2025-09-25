import pandas as pd
import mysql.connector

# --------------------------
# Step 1: Load your CSV data
# --------------------------
csv_file_path = "C:/Users/B santosh/Downloads/ola/Ola_ride_/Dataset/OLA_DataSet_Cleaned.csv"
df = pd.read_csv(csv_file_path)

# --------------------------
# Step 2: Connect to MySQL (without specifying database yet)
# --------------------------
conn = mysql.connector.connect(
    host="ola-ride.cnque8eos4ry.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="Santosh7483",
    port=3306
)
cursor = conn.cursor()

# --------------------------
# Step 3: Create database if it doesn't exist
# --------------------------
cursor.execute("CREATE DATABASE IF NOT EXISTS ola_ride_db")
cursor.execute("USE ola_ride_db")

# --------------------------
# Step 4: Create table if it doesn't exist
# --------------------------
create_table_query = """
CREATE TABLE IF NOT EXISTS OLA_Data (
    Date DATE,
    Time TIME,
    Booking_ID VARCHAR(20) PRIMARY KEY,
    Booking_Status VARCHAR(50),
    Customer_ID VARCHAR(20),
    Vehicle_Type VARCHAR(30),
    Pickup_Location VARCHAR(100),
    Drop_Location VARCHAR(100),
    V_TAT INT,
    C_TAT INT,
    Canceled_Rides_by_Customer INT,
    Canceled_Rides_by_Driver INT,
    Incomplete_Rides VARCHAR(5),
    Incomplete_Rides_Reason VARCHAR(100),
    Booking_Value DECIMAL(10,2),
    Payment_Method VARCHAR(30),
    Ride_Distance DECIMAL(8,2),
    Driver_Ratings DECIMAL(3,1),
    Customer_Rating DECIMAL(3,1)
)
"""
cursor.execute(create_table_query)

# --------------------------
# Step 5: Insert CSV data into table
# --------------------------
insert_query = """
INSERT INTO OLA_Data
(Date, Time, Booking_ID, Booking_Status, Customer_ID, Vehicle_Type, Pickup_Location, Drop_Location,
 V_TAT, C_TAT, Canceled_Rides_by_Customer, Canceled_Rides_by_Driver, Incomplete_Rides,
 Incomplete_Rides_Reason, Booking_Value, Payment_Method, Ride_Distance, Driver_Ratings, Customer_Rating)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convert DataFrame rows to list of tuples
data = [tuple(x) for x in df.to_numpy()]

# Bulk insert using executemany
cursor.executemany(insert_query, data)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("✅ Database, table created and data loaded successfully!")
