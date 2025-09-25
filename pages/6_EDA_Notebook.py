import streamlit as st
import os

st.set_page_config(page_title="EDA Notebook", layout="wide")
st.title("📑 OLA Ride Analysis – EDA Notebook")

# ============================
# File Path (adjust as needed)
# ============================
eda_path = os.path.join("EDA", "EDA_ola_ride_analysis.ipynb")

# ============================
# Download Section
# ============================
st.subheader("📥 Download EDA Notebook")
if os.path.exists(eda_path):
    with open(eda_path, "rb") as f:
        st.download_button(
            label="⬇️ Download EDA_ola_ride_analysis.ipynb",
            data=f,
            file_name="EDA_ola_ride_analysis.ipynb",
            mime="application/octet-stream"
        )
else:
    st.error("⚠️ EDA notebook not found. Please check the file path.")

# ============================
# EDA Summary
# ============================
st.subheader("🔍 Summary of EDA Tasks & Insights")

st.markdown("""
### ✅ Tasks Performed
1. **Data Wrangling & Cleaning**
   - Removed duplicates, handled missing values, standardized column formats.
   - Converted dates and times into proper formats.
   - Created cleaned dataset `OLA_DataSet_Cleaned.csv`.

2. **Exploratory Analysis**
   - Ride volume trends over time.
   - Booking status distribution (success, cancellations, driver not found).
   - Vehicle type usage and total ride distances.
   - Revenue analysis by payment method and customer contributions.
   - Cancellation reasons analysis (customer vs. driver).
   - Distribution of ratings, booking values, and ride distances.

3. **Visualization**
   - Bar charts, pie charts, boxplots, violin plots, KDE plots, heatmaps, and scatter plots.
   - Storytelling with insights from each visualization.

---

### 📊 Key Outcomes
- **Ride Demand:** Most rides are concentrated during **evening peak hours (6–8 PM)**.
- **Booking Success Rate:** ~62% rides successful; ~38% failed (mostly driver cancellations).
- **Vehicle Insights:** **Prime Sedan** and **Auto** dominate demand; **eBike** contributes significantly to total ride distance.
- **Revenue Insights:** **Cash** is still dominant, followed by **UPI**; cards have very low usage.
- **Customer Insights:** Top customers drive a large portion of revenue.
- **Ratings:** Both drivers and customers show a **bimodal pattern** at 4.0 and 5.0, indicating generally high satisfaction.
- **Cancellations:** A majority of incomplete rides are marked as *Unknown reason* → signals need for better data capture.

---

### 🎯 Conclusion
This EDA project revealed crucial operational and customer insights:
- Enhance **driver reliability** to reduce cancellations.
- Encourage **digital payment adoption** to minimize cash handling.
- Focus on **popular vehicle types & hotspots** for better fleet allocation.
- Leverage insights from ratings to **improve service quality**.

---

✅ This EDA formed the backbone for the **Power BI Dashboard** and **Streamlit Analytics App**, ensuring data-driven decision making for OLA.
""")
