# 🛍️ Diwali Sales Data Analysis  

## 📌 Problem Statement  
During Diwali, e-commerce companies witness a significant spike in sales. Understanding **customer purchasing behavior** during this festive season can help businesses design better **targeted marketing strategies** and boost revenue.  

The objective of this project is to analyze the **Diwali Sales dataset** to uncover insights such as:  
- Which **age groups** and **genders** contribute most to sales?  
- Which **states** and **occupations** have the highest purchasing power?  
- Which **product categories** and **products** are the most popular?  

---

## 📂 Dataset  
- File: **Diwali Sales Data.csv**  
- Features include:  
  - `User_ID`, `Cust_name`, `Gender`, `Age Group`, `State`, `Occupation`,  
  - `Marital_Status`, `Product_Category`, `Product_ID`, `Orders`, `Amount`  

---

## 🔧 Data Cleaning Steps  
- Dropped unrelated/blank columns (`Status`, `unnamed1`)  
- Removed missing values  
- Converted `Amount` column to integer type  
- Renamed columns for clarity (e.g., `Marital_Status` → `Shaadi`)  

---

## 📊 Exploratory Data Analysis (EDA)  
The analysis was performed using **Python (Pandas, Matplotlib, Seaborn)**.  

### Key Insights  
1. **Gender**  
   - Most buyers are **females**  
   - Females contribute to higher total sales than males  

2. **Age Group**  
   - The **26–35 years** group dominates sales  
   - Within this group, **females** are the highest spenders  

3. **State**  
   - Top states by sales/orders:  
     - **Uttar Pradesh, Maharashtra, Karnataka**  

4. **Marital Status**  
   - **Married women** show the highest purchase behavior  

5. **Occupation**  
   - Major spenders are from **IT, Healthcare, and Aviation** sectors  

6. **Product Category**  
   - Top categories: **Food, Clothing, Electronics**  

7. **Top Products**  
   - A handful of products contribute significantly to total sales  

---

## ✅ Conclusion & Business Recommendation  
- Target audience: **Married women (26–35 years old)**  
- Focused marketing in **Uttar Pradesh, Maharashtra, and Karnataka**  
- Promote offers in **Food, Clothing, and Electronics** categories  
- Personalized campaigns for **IT, Healthcare, and Aviation** professionals  

👉 By leveraging these insights, e-commerce companies can **optimize ad spending, improve targeting, and maximize revenue** during Diwali sales.  

---

## ⚙️ Tech Stack  
- **Python** (Pandas, NumPy)  
- **Visualization**: Matplotlib, Seaborn  
- **Jupyter Notebook** for analysis  

---

## 📁 Project Structure  

