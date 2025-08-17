# 🛒 Amazon Sales Data Analysis

## 📌 Problem Statement
E-commerce platforms like Amazon generate massive amounts of transactional data every day.  
To make informed business decisions, it is important to analyze this sales data and uncover patterns such as:
- Which product categories are performing well?
- What are the most preferred product sizes?
- How much do B2B orders contribute compared to retail orders?
- Which states contribute the highest sales volume?

The goal of this project is to **clean, analyze, and visualize Amazon sales data** to derive insights that can guide inventory, marketing, and fulfillment strategies.

---

## 🎯 Project Objectives
- Perform **data cleaning & preprocessing** for accurate analysis.  
- Conduct **exploratory data analysis (EDA)** to identify trends in sales.  
- Visualize results for easier interpretation.  
- Highlight key **metrics** useful for decision-making.  

---

## 📂 Dataset
- **File:** `Amazon Sale Report.csv`  
- **Rows:** 128,976 → cleaned to 37,514 after removing nulls  
- **Columns:** 21 → cleaned to 19 after dropping irrelevant ones  
- **Time Period:** April 2022 – June 2022  

---

## 🧹 Data Cleaning Steps
1. Dropped irrelevant/blank columns: `New`, `PendingS`  
2. Removed rows with **null values** → final dataset size = `37,514 rows × 19 columns`  
3. Converted `ship-postal-code` → integer type  
4. Converted `Date` → datetime format  
5. Renamed columns (`Qty` → `Quantity`)  

---

## 🔍 Exploratory Data Analysis (EDA)

### 📏 Key Metrics & Findings
1. **Top Product Category** → T-shirts (most purchased category).  
2. **Preferred Product Size** → "M" size dominates, followed by "L" and "XL".  
3. **Order Fulfillment** → Amazon (Easy Ship) handles majority of deliveries.  
4. **Customer Segment** → 99.3% orders from Retail buyers, only 0.7% from B2B.  
5. **Top State by Sales** → Maharashtra contributes the highest sales volume.  

---

## 📊 Visual Insights

### 1️⃣ Product Size Preference
![Size Distribution]("Amazone-sales/Screenshot 2025-08-17 155251.png")

### 2️⃣ Product Category
![Category Distribution](images/category_distribution.png)

### 3️⃣ Courier & Fulfillment
![Courier Status](images/courier_status.png)

### 4️⃣ B2B vs Retail
![B2B Pie](images/b2b_pie.png)

### 5️⃣ Geographic Distribution
![Top States](images/top_states.png)

---

## ✅ Conclusion
- **T-shirts (M-size)** are the most purchased products.  
- Sales are heavily concentrated in **Maharashtra**.  
- **Amazon’s Easy Ship service** is the dominant fulfillment method.  
- Very few customers are **B2B buyers**, indicating retail dominates this dataset.  

**Future Work:**
- Perform **time series analysis** to forecast demand.  
- Build a **predictive ML model** for sales forecasting.  
- Create an interactive **dashboard** in Power BI or Tableau.  

---

## 🚀 Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn)  
- Jupyter/Colab Notebook  

---

## 📂 Repository Structure
