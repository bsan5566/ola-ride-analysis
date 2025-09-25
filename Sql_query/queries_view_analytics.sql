use ola_ride;
-- SEGREGATING THE VIEWS
-- ===========================
-- 1. OVERALL
-- ===========================

-- Ride Volume Over Time
CREATE VIEW Ride_Volume_Over_Time AS
SELECT Date, COUNT(*) AS Total_Rides
FROM OLA_Data
GROUP BY Date
ORDER BY Date;

-- Booking Status Breakdown
CREATE VIEW Booking_Status_Breakdown AS
SELECT Booking_Status, COUNT(*) AS Total_Bookings
FROM OLA_Data
GROUP BY Booking_Status;


-- ===========================
-- 2. VEHICLE TYPE
-- ===========================

-- Top 5 Vehicle Types by Ride Distance
CREATE VIEW Top_5_Vehicle_Types_Distance AS
SELECT Vehicle_Type, SUM(Ride_Distance) AS Total_Distance
FROM OLA_Data
GROUP BY Vehicle_Type
ORDER BY Total_Distance DESC
LIMIT 5;


-- ===========================
-- 3. REVENUE
-- ===========================

-- Revenue by Payment Method
CREATE VIEW Revenue_By_Payment AS
SELECT Payment_Method, SUM(Booking_Value) AS Total_Revenue
FROM OLA_Data
WHERE Booking_Status = 'Success'
GROUP BY Payment_Method;

-- Top 5 Customers by Total Booking Value
CREATE VIEW Top_5_Customers_Revenue AS
SELECT Customer_ID, SUM(Booking_Value) AS Total_Spending
FROM OLA_Data
WHERE Booking_Status = 'Success'
GROUP BY Customer_ID
ORDER BY Total_Spending DESC
LIMIT 5;

-- Ride Distance Distribution Per Day
CREATE VIEW Ride_Distance_Per_Day AS
SELECT Date, SUM(Ride_Distance) AS Total_Distance
FROM OLA_Data
GROUP BY Date
ORDER BY Date;


-- ===========================
-- 4. CANCELLATION
-- ===========================

-- Cancelled Rides by Customers
CREATE VIEW Cancelled_Rides_Customers AS
SELECT Incomplete_Rides_Reason, COUNT(*) AS Total_Customer_Cancellations
FROM OLA_Data
WHERE Booking_Status = 'Canceled by Customer'
GROUP BY Incomplete_Rides_Reason;

-- Cancelled Rides by Drivers
CREATE VIEW Cancelled_Rides_Drivers AS
SELECT Incomplete_Rides_Reason, COUNT(*) AS Total_Driver_Cancellations
FROM OLA_Data
WHERE Booking_Status = 'Canceled by Driver'
GROUP BY Incomplete_Rides_Reason;


-- ===========================
-- 5. RATINGS
-- ===========================

-- Average Driver Ratings per Vehicle Type
CREATE VIEW Avg_Driver_Ratings AS
SELECT Vehicle_Type, AVG(Driver_Ratings) AS Avg_Driver_Rating
FROM OLA_Data
GROUP BY Vehicle_Type;

-- Average Customer Ratings per Vehicle Type
CREATE VIEW Avg_Customer_Ratings AS
SELECT Vehicle_Type, AVG(Customer_Rating) AS Avg_Customer_Rating
FROM OLA_Data
GROUP BY Vehicle_Type;

SHOW FULL TABLES IN ola_ride WHERE table_type = 'VIEW';

