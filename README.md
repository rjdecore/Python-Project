# Python Data Analytics Portfolio

A collection of Python projects focused on data preparation, exploratory analysis, visualization, customer/product behavior, time trends and text analysis.

**Core stack:** Python · Pandas · NumPy · Matplotlib · Seaborn · Plotly · Jupyter/Colab

## Featured projects

| Project | Business question | Main workflow |
|---|---|---|
| [Amazon Sales Analysis](Amazone-sales/) | How do product categories, sizes, fulfillment and geography vary in the order data? | Data cleaning, datetime preparation, grouped analysis, visualization |
| [Diwali Sales Analysis](project-1/Diwali_Sales_Analysis/) | How do customer segments, geography and product categories vary in the festive-season data? | Missing-value review, segment analysis, aggregation, visualization |
| [Uber Ride Analysis](Uber-Data/) | How do ride purposes, time of day, weekday and trip distance vary? | Timestamp parsing, feature creation, missing-value handling, EDA |
| [Google Search Trends](Google_Search_Trend_Analysis/) | How does search interest change over time and across keywords? | Time-series preparation, comparison and visualization |
| [Netflix Content Analysis](Netflix-Data-Analysis/) | What patterns appear in content type, contributors, production years and descriptions? | Categorical analysis, trends, text sentiment |
| [Bank Marketing Analysis](Bank_Data_Analysis-/) | How do customer and campaign characteristics vary in the marketing data? | Cleaning, grouping, category comparisons and EDA |

## Analytical workflow

1. Understand the dataset, row grain and business question.
2. Inspect shape, columns, data types, missing values, duplicates and suspicious values.
3. Make cleaning decisions explicit and measure how many rows each decision removes.
4. Create derived features only when their definitions are clear.
5. Analyze distributions, segments and time trends.
6. Visualize the finding with appropriate labels and units.
7. Write a short interpretation, caveat and next question.

## Skills represented

- Pandas and NumPy
- Data cleaning and feature preparation
- Grouped, categorical and time-based analysis
- Visualization and exploratory data analysis
- Text analysis and sentiment classification where implemented

## Quality notes

For each project, document the original row count, retained row count and reason for each exclusion. Do not remove all rows containing any null by default without checking whether the missing field is essential. Label charts with units, explain the observation period and distinguish correlation/descriptive patterns from causal claims.

Project READMEs describe the intended analysis; verify notebook outputs and calculations before quoting numerical findings in an interview.
