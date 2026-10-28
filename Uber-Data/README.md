# Uber Ride Pattern Analysis — Python

## Business Objective
Analyze ride behavior to understand ride categories, purposes, demand timing, seasonality, weekdays, and trip-distance patterns.

## Dataset
**1,156 rows** with start/end timestamps, category, locations, miles, and ride purpose.

## Key Findings
- Business rides dominate the dataset.
- Meetings are the leading ride purpose.
- Afternoon and evening show peak activity.
- Friday has the highest booking volume.
- Most rides are within 20 miles.
- Winter months show lower demand in the analyzed data.

## Data Preparation
- Converted timestamps to datetime
- Filled missing purpose values
- Created date/time/day/month/day-night features
- Removed remaining nulls after transformation

## Tech Stack
**Python | Pandas | NumPy | Matplotlib | Seaborn | EDA | Time Analysis**