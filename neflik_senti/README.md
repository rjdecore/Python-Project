# Netflix Content & Sentiment Analysis — Python

## Business Objective
Explore Netflix's catalog to understand ratings, contributors, production trends, and sentiment patterns in content descriptions.

## Dataset
**8,807 records** with title, type, director, cast, country, release year, rating, duration, genre, and description.

## Data Preparation
- Filled missing director/cast values
- Split multi-valued director/cast fields
- Excluded placeholder director values from frequency analysis

## Analysis
- Content-rating distribution
- Top directors
- Top actors
- Movie vs TV production trends
- Description sentiment by year

## Sentiment Method
TextBlob polarity is used to classify descriptions as **Positive, Neutral, or Negative**.

## Tech Stack
**Python | Pandas | NumPy | Plotly Express | TextBlob | EDA | NLP**

## Key Findings & Business Value
The analysis describes catalog ratings, contributor frequency, content-type trends and sentiment polarity in title descriptions. Sentiment from plot descriptions is not the same as audience sentiment or viewer satisfaction; use it only as a text-feature demonstration.

Content teams can use the catalog summaries to frame portfolio questions and investigate how descriptions vary across categories and years.

## Report / PDF
[Open the notebook PDF export](Netflix_Data_Analysis.ipynb%20-%20Colab.pdf) with the notebook and source data.
