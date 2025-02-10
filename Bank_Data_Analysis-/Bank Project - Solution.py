#!/usr/bin/env python
# coding: utf-8

# # Questions
# 1. How many married individuals are unemployed?
# 
# 2. What is the average age of individuals who subscribed to a term deposit versus those who did not?
# 
# 3. How does the average balance vary across different contact months?
# 
# 4. How does the average duration of customer calls vary by month?
# 
# 5. What is the distribution of marital status (married/single/divorced) across different education levels?

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


import pandas as pd

data = pd.read_csv(r'D:\Python Project - Dataset\bank.csv')

print(data)


# In[3]:


df = data.copy()


# In[4]:


df.head()


# In[5]:


df.columns


# In[6]:


df = data.copy()
df.columns = df.columns.str.title()
df


# In[7]:


df.columns


# In[8]:


df.rename(columns = {'Marital' : 'Marital_Status',
                     'Pdays' : 'Days_Since_Last_Contact ',
                    'Poutcome':'Previous_Outcome',
                    'Y': 'Customer_Subscription'}, inplace = True)


# In[9]:


df.shape


# In[10]:


df.info()


# In[11]:


df.describe()


# In[12]:


df.describe(include=['O'])


# In[13]:


df.describe(include = 'all')


# # Data Cleaning

# In[14]:


df.dtypes


# In[15]:


df['Job'] = df['Job'].astype('category')
df['Marital_Status'] = df['Marital_Status'].astype('category')
df['Education'] = df['Education'].astype('category')
df['Default'] = df['Default'].astype('category')
df['Housing'] = df['Housing'].astype('category')
df['Loan'] = df['Loan'].astype('category')
df['Contact'] = df['Contact'].astype('category')
df['Month'] = df['Month'].astype('category')
df['Previous_Outcome'] = df['Previous_Outcome'].astype('category')
df['Customer_Subscription'] = df['Customer_Subscription'].astype('category')


# In[16]:


df.dtypes


# In[17]:


df.nunique()


# In[18]:


df_duplicated = df.duplicated()
print(df_duplicated)


# In[19]:


df.duplicated().sum()


# In[20]:


df.drop_duplicates(inplace = True)


# In[21]:


df.duplicated().sum()


# In[22]:


df['Job'].value_counts(normalize = True, ascending = True)


# In[23]:


df.isnull().sum()


# In[24]:


df.isnull().sum()/len(df)* 100


# In[25]:


df['Balance']


# In[26]:


df['Balance'].mode()


# In[27]:


df_Balance = df['Balance'].mean()
df['Balance'] = df['Balance'].fillna(df['Balance'].mean())
df['Balance'].isna().sum()


# In[28]:


df['Campaign'].unique()


# In[29]:


df['Campaign'].mode()


# In[30]:


df['Campaign'] = df['Campaign'].fillna(df['Campaign'].mode()[0])
#Using [0] extracts the first (and typically only) mode value to fill the missing values.


# In[31]:


df['Campaign'].isnull().sum()


# In[32]:


df.isnull().sum()


# In[33]:


df.info()


# # Data Visualization

# 1. How many married individuals are unemployed?
# 
# 2. What is the average age of individuals who subscribed to a term deposit versus those who did not?
# 
# 3. How does the average balance vary across different contact months?
# 
# 4. How does the average duration of customer calls vary by month?
# 
# 5. What is the distribution of marital status (married/single/divorced) across different education levels?

# # 1. How many married individuals are unemployed?

# In[34]:


df.columns


# In[35]:


# Filter the dataset for married individuals who are unemployed
married_unemployed = df[(df['Marital_Status'] == 'married') & (df['Job'] == 'unknown')]

# Count the number of married unemployed individuals
count_married_unemployed = married_unemployed.shape[0]
print(f"Number of married unemployed individuals: {count_married_unemployed}")


# In[36]:


# Visualization: Pie chart
sizes = [count_married_unemployed, df.shape[0] - count_married_unemployed]
plt.pie(sizes, labels=['Married Unemployed', 'Other'], autopct='%1.1f%%', startangle=90,
        colors=['#ff6666', '#66b3ff'], explode=(0.1, 0), shadow=True, wedgeprops={'edgecolor': 'black'})
plt.title('Proportion of Married Unemployed Individuals', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(r"D:\Python Project - Dataset\chart.png", dpi=300, bbox_inches='tight')
plt.show()


# # Report
# The analysis identifies the number of married unemployed individuals in the dataset by filtering for married individuals with an 'unknown' job status. The result is visualized using a pie chart to show the proportion of married unemployed individuals compared to the rest. The chart highlights that a small subset of the population falls into this category. This provides insights into the distribution of employment status among married individuals. The visualization aids in understanding the relationship between marital status and employment.

# # 2. What is the average age of individuals who subscribed to a term deposit versus those who did not?

# In[37]:


# Calculate the average age for both groups: Subscribed and Not Subscribed
avg_age_subscribed = df[df['Customer_Subscription'] == 'yes']['Age'].mean()
avg_age_not_subscribed = df[df['Customer_Subscription'] == 'no']['Age'].mean()


# In[38]:


# Data for pie chart
labels = ['Subscribed', 'Not Subscribed']
average_ages = [avg_age_subscribed, avg_age_not_subscribed]

# Create a pie chart
plt.figure(figsize=(10,6))
plt.pie(average_ages, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#ff9999'])

# Adding title
plt.title('Average Age of Individuals Who Subscribed vs. Did Not Subscribe to a Term Deposit', fontsize=16, fontweight='bold')

# Show the plot
plt.savefig(r"D:\Python Project - Dataset\chart1.png", dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()


# # Report
# The analysis compares the average age of individuals who subscribed and those who did not to a term deposit using a pie chart. The chart highlights the demographic differences between the two groups. It shows that individuals who subscribed have a distinct average age compared to those who did not. This information can help refine marketing strategies targeted at specific age groups. The visualization provides a clear view of the age distribution in relation to term deposit subscriptions..

# # 3. How does the average balance vary across different contact months?

# In[39]:


# Group by 'Month' and calculate the average balance for each month
avg_balance_per_month = df.groupby('Month')['Balance'].mean()


# In[40]:


# Visualization: Horizontal bar chart for average balance across months with similar colors
plt.figure(figsize=(10,6))
avg_balance_per_month.plot(kind='barh', color=['#66b3ff', '#ff9999', '#66b3ff', '#ff9999', '#66b3ff', '#ff9999', '#66b3ff', '#ff9999', '#66b3ff', '#ff9999', '#66b3ff', '#ff9999'])

# Adding titles and labels
plt.title('Average Balance Across Different Contact Months', fontsize=16, fontweight='bold')
plt.ylabel('Month', fontsize=12)
plt.xlabel('Average Balance', fontsize=12)

# Show the plot
plt.tight_layout()
plt.savefig(r"D:\Python Project - Dataset\chart2.png", dpi=300, bbox_inches='tight')
plt.show()


# # Report
# The analysis shows how the average balance varies across different contact months using a horizontal bar chart. The chart reveals fluctuations in average balance throughout the months, with some months having higher average balances than others. These variations might be linked to seasonal factors or marketing campaigns. The visualization provides insights into customer behavior and financial patterns, which could inform targeted marketing strategies. It also highlights months with significant changes in customer balances.

# # 4. How does the average duration of customer calls vary by month?

# In[41]:


# Group by 'Month' and calculate the average duration of customer calls for each month
avg_duration_per_month = df.groupby('Month')['Duration'].mean()

# Visualization: Line chart for average call duration across months
plt.figure(figsize=(10,6))
avg_duration_per_month.plot(kind='line', marker='o', color='#66b3ff', linestyle='-', linewidth=2)

# Adding titles and labels
plt.title('Average Duration of Customer Calls Across Different Months', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Duration (seconds)', fontsize=12)

# Show the plot
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(r"D:\Python Project - Dataset\chart3.png", dpi=300, bbox_inches='tight')
plt.show()


# # Report
# The analysis shows how the average duration of customer calls varies across different months. The line chart indicates fluctuations in call duration over the year. Some months show longer call durations, while others have shorter averages. This trend could reflect seasonal marketing efforts or customer engagement patterns. The visualization helps understand how call durations change over time, which can be useful for evaluating the effectiveness of campaigns or customer service performance.

# # 5. What is the distribution of marital status (married/single/divorced) across different education levels?

# In[42]:


# Group by 'Education' and 'Marital_Status' to get the count of each marital status for each education level
education_marital_counts = df.groupby(['Education', 'Marital_Status']).size().unstack(fill_value=0)

# Plotting the stacked bar chart
education_marital_counts.plot(kind='bar', stacked=True, color=['#66b3ff', '#ff9999', '#ffcc66'], figsize=(10,6))

# Adding titles and labels
plt.title('Distribution of Marital Status Across Different Education Levels', fontsize=16, fontweight='bold')
plt.xlabel('Education Level', fontsize=12)
plt.ylabel('Number of Individuals', fontsize=12)

# Show the plot
plt.savefig(r"D:\Python Project - Dataset\chart4.png", dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()


# # Report: 
# The analysis visualizes the distribution of marital status across education levels. Higher education levels show a more balanced marital status, while lower levels have more single individuals. This highlights how marital status varies with education. The chart offers valuable insights for demographic analysis and marketing strategies.

# In[ ]:




