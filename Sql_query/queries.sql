-- CREATING THE DATABASE 
create database IF NOT EXISTS ola_ride ;
USE OLA_RIDE; -- SELECT THE DATABASE
-- CREATING THE TABLE
CREATE TABLE IF NOT EXISTS OLA_Data  (
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
    Incomplete_Rides VARCHAR(5),  -- 'Yes' or 'No'
    Incomplete_Rides_Reason VARCHAR(100),
    Booking_Value DECIMAL(10,2),
    Payment_Method VARCHAR(30),
    Ride_Distance DECIMAL(8,2),
    Driver_Ratings DECIMAL(3,1),
    Customer_Rating DECIMAL(3,1)
);


show tables;
-- View the structure of the table
select* from ola_data;

-- COUNT THE TOTAL NUMBER OF ROWS IN THE TABLE
SELECT COUNT(*) AS total_rows
FROM OLA_Data;


-- SQL QUERIES FOR THE OLA RIDE ANALYSIS

-- FIRST QUERY :- RETRIVE ALL  SUCCESSFULL BOOKINGS
SELECT * FROM OLA_DATA WHERE Booking_Status = 'Success';

-- SECOND QUERY :- FIND THE AVERAGE RIDE DSITANCE FOR EACH VEHICLE TYPE
SELECT Vehicle_Type, AVG(Ride_Distance) AS Avg_Distance
FROM OLA_DATA
GROUP BY VEHICLE_TYPE;

-- THIRD QUERY:- FET THE TOTAL NUMBER OF CANCELLED RIDES BY CUSTOMER
SELECT COUNT(*) AS Total_Customer_Cancellations
FROM  ola_data WHERE Booking_Status = 'Canceled by Customer';

-- FOURTH QUERY :- LIST THE TOP 5 CUSTOMERS WHO BOOKED HIGHEST NUMBER OF RIDES
select CUSTOMER_ID,COUNT(*) AS Total_Rides from ola_data 
GROUP BY Customer_ID
ORDER BY Total_Rides DESC
LIMIT 5;

-- FIFTH QUERY :- Get the number of rides cancelled by drivers due to personal and car-related issues
SELECT INCOMPLETE_RIDES_REASON, COUNT(*) AS Total_Driver_Cancellations
FROM ola_data
WHERE Booking_Status = 'Cancelled by Driver'
AND Incomplete_Rides_Reason IN ('Personal','Car Issue')
GROUP BY Incomplete_Rides_Reason;

-- SIXTH QUERY:- Find the maximum and minimum driver ratings for Prime Sedan bookings
SELECT MAX(Driver_Ratings) AS MAX_RATINGS,
	MIN(Driver_Ratings) AS MIN_RATINGS
    FROM OLA_DATA
	WHERE Vehicle_Type = 'Prime Sedan';
    
    -- SEVENTH QUERY :- RETRIVE ALL RIDES WHERE PAYMENT WAS MADE BY UPI
    SELECT * FROM OLA_DATA WHERE Payment_Method = "UPI";
    
    -- EIGTH QUERY:-  FIND THE AVERAGE CUSTOMER RATING PER VEHICLE TYPE
    SELECT Vehicle_Type, AVG(Customer_Rating) AS AVG_CUSTOMER_RATING
    FROM ola_data GROUP BY Vehicle_Type;
    
    -- NINTH QUERY :- Calculate the total booking value of rides completed successfully
    SELECT SUM(Booking_Value) AS Total_Successful_Revenue FROM OLA_DATA
    WHERE Booking_Status = 'Success';
    
    -- Tenth Query :- List all incomplete rides along with the reason
SELECT Booking_ID, Customer_ID, Vehicle_Type, Incomplete_Rides, Incomplete_Rides_Reason
FROM OLA_Data
WHERE Incomplete_Rides = 'Yes';
