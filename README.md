# Ola Ride Analytics

## 📖 Overview
Ola Ride Analytics is an interactive data analytics project built using **Streamlit**.  
The project explores ride data (from `.csv` and `.xlsx` datasets), performs exploratory data analysis (EDA), runs SQL queries, and visualizes results.  
It also integrates **Power BI** dashboards for advanced insights.

## 📂 Project Structure
```
Ola_ride/
│── app.py                       # Main Streamlit application
│
├── pages/                       # Streamlit multipage app
│   ├── 1_Home.py
│   ├── 2_Dataset_Preview.py
│   ├── 3_Sql_Queries.py
│   ├── 4_PowerBI_Question_analytics.py
│   ├── 5_View_Analytics.py
│   └── 6_EDA_Notebook.py
│
├── Database/
│   └── db.py                    # Database connection logic
│
├── Dataset/
│   ├── OLA_DataSet.xlsx
│   └── OLA_DataSet_Cleaned.csv
│
├── EDA/
│   └── EDA_ola_ride_analysis.ipynb  # Jupyter notebook for analysis
│
├── Sql_query/
│   ├── queries.sql
│   └── queries_view_analytics.sql
│
├── PowerBi_Files/
│   ├── ola.pbix
│   └── ola_ride_views.pbix
│
└── OLA RIDE.docx                 # Project documentation
```

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Ola_ride.git
   cd Ola_ride
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) If you want to run Jupyter notebooks:
   ```bash
   jupyter notebook
   ```

## ▶️ Usage
To start the Streamlit application:
```bash
streamlit run app.py
```

The app will open in your browser, providing:
- 📊 Dataset preview  
- 🔍 SQL query execution  
- 📈 Analytics & EDA  
- 📉 Power BI dashboards  

## 🛠️ Technologies Used
- **Python** (Streamlit, Pandas, NumPy, Matplotlib, Seaborn)  
- **SQL** (queries for ride data)  
- **Power BI** (dashboards)  
- **Excel/CSV** (datasets)  

## ✨ Features
- Interactive ride dataset exploration  
- SQL-based analytics  
- Visual insights through charts  
- Power BI integration  
- Notebook-based EDA  
