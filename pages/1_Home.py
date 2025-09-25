import streamlit as st

st.set_page_config(page_title="OLA Ride Insights - Project Overview", layout="wide")

st.title("🏠 OLA Ride Insights - Project Overview")

st.markdown("""
---

### 📌 Project Name  
**OLA_RIDE_ANALYSIS**

---

### 📝 Problem Statement  
The rise of ride-sharing platforms has transformed urban mobility, offering convenience and affordability to millions of users.  
**OLA**, a leading ride-hailing service, generates vast amounts of data related to ride bookings, driver availability, fare calculations, and customer preferences.  

However, deriving actionable insights from this data remains a challenge. To enhance operational efficiency, improve customer satisfaction, and optimize business strategies, this project focuses on analyzing OLA’s ride-sharing data.  

By leveraging **data analytics, visualization techniques, and interactive applications**, the goal is to extract meaningful insights that can drive **data-informed decisions**.  

The project involves:  
- Cleaning and processing raw ride data  
- Performing exploratory data analysis (EDA)  
- Developing a dynamic Power BI dashboard  
- Creating a Streamlit-based web application to present findings interactively  

---

### 🎯 Objectives  
- Identify **peak demand patterns** and optimize driver allocation  
- Understand **customer behavior & preferences**  
- Analyze **pricing & revenue patterns**  
- Detect and explain **cancellation reasons**  
- Measure **service quality** using ratings  

---

### 🛠️ Tools & Technologies  
- **SQL** → Data extraction & preprocessing  
- **Python (Pandas, Matplotlib, Seaborn)** → Data wrangling & EDA  
- **Power BI** → Interactive dashboard visualization  
- **Streamlit + Plotly** → Web-based analytics & storytelling  

---

👉 Use the **sidebar navigation** to explore:  
- 🗂 Dataset Preview  
- 📥 SQL Queries Runner 
- 📊 View analytics Dashboard  
- 📈 Power BI Questions & Visuals  
- 📑 EDA Report & Notebook  
---
### The downloadable files are available in the respective sections.
- **Dataset files** in the "Dataset Preview" section
- **SQL Queries** in the "SQL Queries" section
- **Power BI Report** in the "Power BI Questions" section
- View Analysis in "View Analytics" section
- **EDA Notebook** in the "EDA Report & Notebook" section

""")
