# 🌤️ Weather Data Analysis (2012 Dataset)

## 📌 Project Overview
This project is a comprehensive **Exploratory Data Analysis (EDA)** on a weather dataset from 2012.  
Using **Python, Pandas, NumPy, Matplotlib, and Seaborn**, we analyze various aspects of the weather such as **temperature, humidity, visibility, wind speed, and weather conditions**.  

The goal is to clean, process, and analyze the dataset while answering a set of predefined analytical questions with both tabular and visual outputs.

---

## 📂 Dataset Information
- **Source:** CSV file containing hourly weather records of 2012  
- **Total Records:** 8784 rows  
- **Columns:**  

| Column             | Description |
|--------------------|-------------|
| Date/Time          | Timestamp of observation |
| Temp_C             | Temperature in Celsius |
| Dew Point Temp_C   | Dew Point Temperature in Celsius |
| Rel Hum_%          | Relative Humidity (%) |
| Wind Speed_km/h    | Wind Speed in km/h |
| Visibility_km      | Visibility in km |
| Press_kPa          | Atmospheric Pressure in kPa |
| Weather Condition  | Weather condition description |

---

## 🧹 Data Cleaning Steps
- ✅ Converted **`Date/Time`** column to proper datetime format  
- ✅ Checked for **missing values** (none found)  
- ✅ Renamed column **`Weather` → `Weather Condition`** for clarity  
- ✅ Converted data types for consistency  

---

## 🔎 Exploratory Analysis & Questions Answered

We answered **15 key questions** about the dataset:

1. **Unique Wind Speeds** → Listed all unique values, plotted bar chart  
2. **Weather Exactly Clear** → Found **1326 instances**  
3. **Wind Speed Exactly 4 km/h** → Found **474 instances**  
4. **Null Values** → None found (validated with heatmap)  
5. **Renamed Column** → `Weather` → `Weather Condition`  
6. **Mean Visibility** → **27.66 km**  
7. **Standard Deviation of Pressure** → **0.844 kPa**  
8. **Variance of Relative Humidity** → **286.25**  
9. **Snow Records** → **390 instances**  
10. **Wind Speed > 24 & Visibility = 25** → **308 records**  
11. **Mean Values by Weather Condition** → Grouped stats calculated  
12. **Min & Max Values by Weather Condition** → Tabulated  
13. **Records with Fog** → **150 rows**  
14. **Weather Clear or Visibility > 40** → **313 rows**  
15. **Complex Condition** → Extracted rows where:  
   - (A) Weather = Clear & Humidity > 50  
   - (B) Visibility > 40  

---

## 📊 Visualizations
Some plots used in this project:
- 📌 Distribution of **wind speeds**  
- 📌 Bar charts for **Clear, Snow, Fog conditions**  
- 📌 Heatmap of **missing values**  
- 📌 Aggregated **mean/variance plots**  

---

## 🛠️ Tools & Libraries Used
- 🐍 **Python 3**  
- 🐼 **Pandas** → Data manipulation & cleaning  
- 🔢 **NumPy** → Numerical analysis  
- 📈 **Matplotlib / Seaborn** → Visualizations  

---

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/weather-data-analysis.git
