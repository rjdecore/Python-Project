# Amazon Sales Data Analysis — Python

## Objective
Explore Amazon order records from April–June 2022 to understand product mix, size demand, fulfillment status, B2B mix and shipping geography.

## Dataset and grain
- Source: [Amazon Sale Report.csv](Amazon%20Sale%20Report.csv)
- Raw data: 128,976 rows and 21 columns before removing the two blank/irrelevant columns used in the notebook.
- Grain caution: a row is not automatically a unique customer or a successfully delivered order. Check Order ID uniqueness and order status before translating record counts into customer or delivery claims.

## Questions explored
- Which sizes and categories occur most often, and how does quantity differ from record count?
- How are records distributed by courier status and order status?
- What is the B2B versus retail mix?
- Which shipping states have the most records?
- How does Amount vary across frequently occurring categories?

## Data preparation
The notebook removes the blank/irrelevant New and PendingS columns, converts Amount and quantity fields to numeric, preserves missing optional fields, converts the postal-code field to a nullable integer, parses dates using the source format, and renames Qty to Quantity. Postal codes are identifiers rather than measurements, so they should not be averaged or treated as a numeric business metric.

The notebook deliberately avoids dropping every row with any missing value. Instead, it surfaces missingness and uses question-specific filters where needed.

## Visual analysis
- Size frequency and total quantity
- Amount distribution
- Top categories by record count
- Courier status versus order status
- B2B/retail and fulfillment mix
- Shipping-state record counts
- Order-amount distribution across the five most frequent categories

## Interpretation and limitations
The notebook is an exploratory analysis. Rankings and percentages should be reproduced by running the current notebook against the included CSV. Counts are described as records/order lines unless explicitly deduplicated by Order ID. A high number of records does not automatically mean a high number of unique customers, and status mix should be checked before describing demand as completed sales.

## Files
- [Analysis notebook](Amazon%20Sale%20Report.ipynb)
- [Source CSV](Amazon%20Sale%20Report.csv)
- [Notebook PDF export](Amazon%20Sale%20Report.ipynb%20-%20Colab.pdf)
- PNG files contain earlier chart exports; rerun the notebook before treating them as the current results.

## Business value
This analysis can help frame questions about assortment, size availability, fulfillment mix and geographic demand. Any stock or campaign decision should be based on validated order-level metrics and current data, not chart appearance alone.

## Stack
Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook.
