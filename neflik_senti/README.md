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