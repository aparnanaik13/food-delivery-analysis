#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[4]:


file_path = 'food_orders.csv'

food_orders = pd.read_csv(file_path)


# In[5]:


food_orders.head()


# In[6]:


food_orders.info()


# - The dataset contains 1000 entries and 12 columns, with no missing values in any of the columns.

# Data Cleaning and Preparation
# - Convert 'Order Date and Time' and 'Delivery Date and Time' to a datetime format. 
# - Convert 'Discounts and Offers' to a consistent numeric value.
# - Ensure all monetary values are in a format that allows calculations.

# In[7]:


from datetime import datetime

food_orders['Order Date and Time'] = pd.to_datetime(food_orders['Order Date and Time'])
food_orders['Delivery Date and Time'] = pd.to_datetime(food_orders['Delivery Date and Time'])


# In[8]:


def extract_discount(x):
    x = str(x)
    if 'off' in x:
        return float(x.split(' ')[0])
    elif '%' in x:
        return float(x.split('%')[0])
    else:
        return 0.0
    
# Applying the function to Create a New Column 'Discount Percentage'
food_orders['Discount Percentage'] = food_orders['Discounts and Offers'].apply(lambda x: extract_discount(x))

# Calculate the Discount Amount
food_orders['Discount Amount'] = food_orders.apply(lambda x: (x['Order Value'] * x['Discount Percentage'] / 100)
                                                   if x['Discount Percentage'] > 1 # if discount percentage is greater than 1, calculate discount amount based on the order value
                                                   else x['Discount Percentage'], axis=1) # use the discount percentage as the discount amount

# Adjust 'Discount Amount' for Fixed Discounts
food_orders['Discount Amount'] = food_orders.apply(lambda x: x['Discount Amount'] if x['Discount Percentage'] <= 1 # keep 'Discount Amount' as is
                                                   else x['Order Value'] * x['Discount Percentage'] / 100, axis=1) # recalculate the discount amount based on the order value and discount percentage

print(food_orders[['Order Value', 'Discounts and Offers', 'Discount Percentage', 'Discount Amount']].head(), food_orders.dtypes)


# - 'Order Date and Time' and 'Delivery Date and Time' columns have been converted to datetime format.
# - 'Discount Percentage' has been added to represent the discount rate or fixed amount discount directly.
# - 'Discount Amount' has been calculated based on the 'Discounts and Offers' column by extracting percentage discounts and fixed amounts, and applying them to the 'Order Value'. 

# In[11]:


food_orders.head()


# Cost and Profitability Analysis
# - Delivery Fee: Fee charged for delivering the order.
# - Payment Processing Fee: Fee for processing the payment.
# - Discount Amount: provided on the order.

# In[9]:


# Total costs and revenue per order
food_orders['Total Costs'] = food_orders['Delivery Fee'] + food_orders['Payment Processing Fee'] + food_orders['Discount Amount']
food_orders['Revenue'] = food_orders['Commission Fee']
food_orders['Profit'] = food_orders['Revenue'] - food_orders['Total Costs']

# Aggregate the data to get the overall metrics
total_orders = food_orders.shape[0]
total_revenue = food_orders['Revenue'].sum()
total_costs = food_orders['Total Costs'].sum()
total_profit = food_orders['Profit'].sum()

overall_total = {
    "Total Orders": total_orders,
    "Total Revenue": total_revenue,
    "Total Costs": total_costs,
    "Total Profit": total_profit
}

print(overall_total)


# In[29]:


food_orders.head()


# In[14]:


import matplotlib.pyplot as plt

# Histogram of profits per order
plt.figure(figsize=(10,6))
plt.hist(food_orders['Profit'], bins=50, color='blue', edgecolor='black')
plt.title('Profit Distribution per Order in Food Delivery')
plt.xlabel('Profit')
plt.ylabel('Number of Orders')
plt.axvline(food_orders['Profit'].mean(), color='red', linestyle='dashed', linewidth=1)
plt.show()


# - This shows a wide distribution of profit per order, with a number of orders resulting in a loss (profits below 0). The average profit is in the negative territory, displaying the overall loss-making situation.

# In[21]:


# Pie chart showing the proportion of total costs
costs_breakdown = food_orders[['Delivery Fee', 'Payment Processing Fee', 'Discount Amount']].sum()
plt.figure(figsize=(7, 7))
plt.pie(costs_breakdown, labels=costs_breakdown.index, autopct='%1.1f%%', startangle=140, colors=['#66c2a5', '#fc8d62', '#8da0cb'])
plt.title('Proportion of Total Costs in Food Delivery')
plt.show()


# - The pie chart illustrates the breakdown ot the total costs into delivery fees, payment processing fees, and discount amounts. 
# - Discounts constitute a large portion of the costs, suggesting that promotional strategies might be heavily impacting overall profitability.

# In[23]:


# Bar chart for total revenue, costs and profit
totals = ['Total Revenuw', 'Total Costs', 'Total Profit']
values = [total_revenue, total_costs, total_profit]

plt.figure(figsize=(8, 6))
plt.bar(totals, values, color=['#66c2a5', '#fc8d62', '#8da0cb'])
plt.title('Total Revenue, Costs, and Profit')
plt.ylabel('Amount (INR)')
plt.show()


# - The bar chart compares the total revenue, total costs, and total profit. It visually represents the gap between the revenue and costs, showing that the costs excel the revenue, leading to a loss.

# New Strategy for Profits

# - New average commission percentage based on the profitable orders.
# - New average discount percentage for profitable orders.

# In[31]:


# Filter the dataset for profitable orders
profitable_orders = food_orders[food_orders['Profit'] > 0].copy()

# Calculate the average commission percentage for profitable orders
profitable_orders.loc[:, 'Commission Percentage'] = (profitable_orders['Commission Fee'] / profitable_orders['Order Value']) * 100

# Calculate the average discount percentage for profitable orders
profitable_orders.loc[:, 'Effective Discount Percentage'] = (profitable_orders['Discount Amount'] / profitable_orders['Order Value']) * 100

# Calculate the new averages
new_average_commission_percentage = profitable_orders['Commission Percentage'].mean()
new_average_discount_percentage = profitable_orders['Effective Discount Percentage'].mean()

print("New Average Commission Percentage:", new_average_commission_percentage)
print("New Average Discount Percentage:", new_average_discount_percentage)


# - The analysis shows that profitable orders have a higher average commission rate and a lower average discount rate compared to overall orders. This suggests that increasing the commission rate to around 30% and reducing the discount rate to about 6% could improve profitability.

# Comparing Profitability: Actual vs. Recommended Discounts and Commissions.

# 1. Calculate profitability per order with actual discounts and commissions.
# 2. Simulate profitability per order with recommended discounts (6%) and commissions (30%) to assess potential impact

# In[32]:


# Set recommended commission and discount percentages
recommended_commission_percentage = 30.0
recommended_discount_percentage= 6.0

# Calculate the commission fee and discount amount using the recommended percentages
food_orders['Simulated Commission Fee'] = food_orders['Order Value'] * (recommended_commission_percentage / 100)
food_orders['Simulated Discount Amount'] = food_orders['Order Value'] * (recommended_discount_percentage / 100)

# Recalculate the total costs and profits for each order using the simulated values
food_orders['Simulated Total Costs'] = (food_orders['Delivery Fee'] +
                                        food_orders['Payment Processing Fee'] +
                                        food_orders['Simulated Discount Amount'])

food_orders['Simulated Profit'] = (food_orders['Simulated Commission Fee'] - food_orders['Simulated Total Costs'])


# In[33]:


food_orders.head()


# In[34]:


import seaborn as sns

plt.figure(figsize=(14, 7))

# Actual profitability
sns.kdeplot(food_orders['Profit'], label='Actual Profitability', fill=True, alpha=0.5, linewidth=2)

# Simulated profitability
sns.kdeplot(food_orders['Simulated Profit'], label='Estimated Profitability with Recommended Rates', fill=True, alpha=0.5, linewidth=2)

plt.title('Comparison of Profitability in Food Delivery: Actual vs. Recommended Discounts and Commissions')
plt.xlabel('Profit')
plt.ylabel('Density')
plt.legend(loc='upper left')
plt.show()


# - The visualization compares actual and estimated profitability per order. The actual distribution shows many orders with losses and varied profit levels. The simulated scenario with recommended discounts (6%) and commissions (30%) shifts towards higher profits, suggesting these adjustments could increase the number of profitable orders.

# In[ ]:




