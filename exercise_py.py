
import pandas as pd

retails_sales_df = pd.read_csv('retail_sales_dataset.csv')

# Q18: Calculate Sales in Another Currency
retails_sales_df['total_amount_usd'] = (
    retails_sales_df['Total Amount'] * 0.055
)

# Q20: Calculate Quantity-to-Age Ratio
retails_sales_df['quantity_age_ratio'] = (
    retails_sales_df['Quantity'] / retails_sales_df['Age']
)

# Q21: Calculate Sales per Item
retails_sales_df['sales_per_item'] = (
    retails_sales_df['Total Amount'] / retails_sales_df['Quantity']
)

# Q22: Calculate Adjusted Sales
retails_sales_df['adjusted_sales'] = (
    (retails_sales_df['Total Amount'] * 0.1)
    + retails_sales_df['Total Amount']
)

# Q23: Calculate Each Transaction's Percentage of Total Sales
retails_sales_df['sales_percentage'] = (
    100 * retails_sales_df['Total Amount']
    / retails_sales_df['Total Amount'].sum()
)

# Q24: Calculate Quantity Percentage
retails_sales_df['quantity_percentage'] = (
    100 * retails_sales_df['Quantity']
    / retails_sales_df['Quantity'].sum()
)

# Q25: Calculate Customer Age Relative to Average Age
retails_sales_df['age_ratio'] = (
    retails_sales_df['Age']
    / retails_sales_df['Age'].mean()
)

# Display the transformed DataFrame
print(retails_sales_df.head(10))
