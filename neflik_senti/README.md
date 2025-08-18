# 🎬 Netflix Content Analysis (EDA + Sentiment Analysis)

## 📌 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on the **Netflix Titles Dataset** using Python.  
The analysis explores **content ratings, directors, actors, content production trends, and sentiment analysis** of show descriptions.  
Visualizations are built using **Plotly Express** for interactive insights.

---

## 📂 Dataset Information
- **Source:** `netflix_titles.csv`  
- **Total Records:** 8807 rows  
- **Columns:**  

| Column       | Description |
|--------------|-------------|
| show_id      | Unique ID of the show |
| type         | Movie / TV Show |
| title        | Title of the content |
| director     | Director(s) |
| cast         | Cast members |
| country      | Country of production |
| date_added   | Date added to Netflix |
| release_year | Year of release |
| rating       | Content rating (e.g., PG, TV-MA) |
| duration     | Duration of movie / seasons |
| listed_in    | Genre(s) |
| description  | Description of content |

---

## 🧹 Data Cleaning
- ✅ Filled missing values in **`director`** with `"Director not specified"`  
- ✅ Filled missing values in **`cast`** with `"No cast specified"`  
- ✅ Split **multi-valued columns** (`director`, `cast`) for frequency analysis  
- ✅ Removed `"Director not specified"` from director count  

---

## 🔎 Analysis Performed

### 1️⃣ Distribution of Content Ratings
- Counted occurrences of each rating category  
- Visualized with an **interactive pie chart**  

### 2️⃣ Top 5 Directors on Netflix
- Extracted director names  
- Counted frequency of direction  
- Displayed **Top 5 directors** with a bar chart  

### 3️⃣ Top 5 Actors on Netflix
- Extracted cast members  
- Counted frequency of appearances  
- Displayed **Top 5 actors** with a bar chart  

### 4️⃣ Trend of Content Production (2000–2021)
- Grouped by **Release Year & Type (Movie/TV Show)**  
- Created a **line graph** showing growth over time  

### 5️⃣ Sentiment Analysis of Descriptions
- Used **TextBlob** to calculate polarity of content descriptions  
- Classified into **Positive, Neutral, Negative**  
- Visualized with a bar chart grouped by year  

---

## 📊 Visualizations
- 📌 Pie chart: Distribution of content ratings  
- 📌 Bar chart: Top 5 directors  
- 📌 Bar chart: Top 5 actors  
- 📌 Line chart: Content produced per year (Movies vs TV Shows)  
- 📌 Sentiment bar chart: Positive/Negative/Neutral content by year  

---

## 🛠️ Tools & Libraries
- 🐍 Python 3  
- 🐼 Pandas → Data manipulation  
- 🔢 NumPy → Numerical operations  
- 📊 Plotly Express → Interactive visualizations  
- 📝 TextBlob → Sentiment analysis  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/netflix-analysis.git
