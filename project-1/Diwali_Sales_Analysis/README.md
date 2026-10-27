# Diwali Sales & Customer Analysis — Python

## Objective
Explore the festive-season sales dataset by customer demographics, state, occupation, marital-status category and product category.

## Business questions
- Which gender and age groups account for the largest recorded order volume and Amount?
- Which states rank highest by order count versus Amount?
- How does recorded sales mix vary by occupation and marital-status category?
- Which product categories lead by record frequency and total Amount?
- Which products appear most often by summed Orders?

## Data preparation
The notebook removes irrelevant columns, checks missingness, validates Amount and Orders as numeric fields, and retains rows where those two measures are available. Missing demographic and category values are labeled Unknown so they are not silently discarded from every analysis. It prints the row counts before and after the numeric-measure filter.

## Analysis
The notebook compares counts and Amount separately for gender, age group, state, marital-status category, occupation and product category, then ranks products by summed Orders.

## Interpretation and limitations
Count and Amount answer different questions: a group can have more records without generating the highest total Amount. The results describe this dataset and do not establish that gender, age, occupation or marital status causes spending behavior. Rerun the notebook to verify retained-row counts and rankings against the included CSV.

## Files
- [Analysis notebook](Diwali_Sales_Analysis%20(1).ipynb)
- [Source dataset](Diwali%20Sales%20Data.csv)

## Business value
The analysis can help form hypotheses for festive assortment and campaign planning. Before making decisions, validate the data period, define whether Orders means transaction count or item quantity, and compare segment size with per-order/per-customer measures.

## Stack
Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook.
