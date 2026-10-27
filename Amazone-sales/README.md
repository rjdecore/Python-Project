# Amazon Sales Data Analysis — Python

## Business Objective

This project analyzes Amazon e-commerce sales data to identify product, customer, fulfillment, and geographic patterns that can support inventory, marketing, and fulfillment decisions.

## Dataset

- **Source file:** `Amazon Sale Report.csv`
- **Raw rows:** 128,976
- **Rows after the documented null-removal step:** 37,514
- **Raw columns:** 21
- **Columns retained after documented cleaning:** 19
- **Period:** April 2022 – June 2022

## Data Preparation

The notebook documents the following preparation steps:

1. Removes irrelevant/blank columns.
2. Handles rows containing null values.
3. Converts `ship-postal-code` to integer type.
4. Converts `Date` to datetime.
5. Renames `Qty` to `Quantity`.

### Data-quality caveat

The documented cleaning step reduces the dataset from **128,976 raw rows to 37,514 rows**. That is a large reduction, so it must be explained before presenting the analysis as production-ready. Check which columns contain nulls, whether those fields are essential for each question, and how many rows each cleaning rule removes. Avoid dropping every row with any null by default if it removes otherwise useful orders. Document the exact exclusion rule and report the retained-row count after each step.

The cleaned dataset is then used for exploratory analysis.

## Business Questions

- Which product categories have the highest order volume?
- Which sizes are most frequently purchased?
- What fulfillment method dominates the dataset?
- What is the mix of B2B versus retail orders?
- Which states contribute the highest sales volume?

## Key Findings

The analysis identifies:

- **T-shirts** as the leading product category.
- **M** as the most common product size.
- **Easy Ship** as the dominant fulfillment method in the dataset.
- A heavily **retail-oriented** customer mix, with the documented analysis reporting approximately 99.3% retail and 0.7% B2B.
- **Maharashtra** as the state with the highest sales volume in the analyzed dataset.

## Visual Analysis

### Product Size

![Size Distribution](Size.png)

### Product Category

![Category Distribution](Category.png)

### Fulfillment

![Fulfillment Analysis](Ship_mode.png)

### B2B vs Retail

![Customer Mix](A.png)

### Geographic Analysis

![State Analysis](State.png)

## Validation checklist before presenting results

- Reproduce the raw and cleaned row counts from the notebook.
- Quantify rows removed by each rule and justify the postal-code type conversion (postal codes are identifiers, not quantities).
- Recalculate the reported retail/B2B mix and state/category rankings from the cleaned data.
- Confirm whether each chart counts orders, order lines, units or sales value; use consistent terminology.
- Check that date filtering matches the documented April–June 2022 period.

## Interview Talking Points

This project demonstrates a practical Python analytics workflow:

**Raw CSV → data cleaning → datatype handling → exploratory analysis → visualization → business interpretation**

The main analytical focus is not only plotting charts, but converting transaction-level data into actionable observations about products, customers, fulfillment, and geography.

## Repository Files

- `Amazon Sale Report.ipynb` — analysis notebook
- `Amazon Sale Report.csv` — source dataset
- `Amazon Sale Report.ipynb - Colab.pdf` — notebook export
- PNG files — analytical visualizations

## Tech Stack

**Python | Pandas | NumPy | Matplotlib | Seaborn | Jupyter/Colab**
