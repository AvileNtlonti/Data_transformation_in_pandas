# Data_transformation_in_pandas
# Retail Sales Data Transformation Using Python and Pandas

## Project Overview

This project focuses on applying **data transformation techniques using Python and Pandas** to a retail sales dataset. The objective is to understand how existing data can be manipulated to create new columns, calculate meaningful metrics, and generate additional insights from sales transactions.

The project covers currency conversion, ratio calculations, percentage analysis, sales adjustments, and the use of statistical aggregation functions within DataFrame transformations.

## Technologies Used

- **Python:** For writing and executing data transformation operations.
- **Pandas:** For loading, manipulating, and analyzing structured datasets.
- **CSV Dataset:** Retail sales data containing customer demographics, product quantities, prices, and transaction amounts.

## Data Transformation Techniques

### 1. Creating New DataFrame Columns

**Concept:** Pandas allows us to create new columns by assigning calculated values to new column names.

**Importance:** This makes it possible to generate additional metrics without modifying or losing the original dataset columns. New features can support deeper analysis, reporting, and data visualization.

### 2. Currency Conversion

Converted transaction amounts into US Dollars using an assumed exchange rate of 1 ZAR = 0.055 USD.

**Importance:** Currency conversion makes financial data easier to compare across different currencies and markets. It is particularly useful when preparing international sales reports.

### 3. Calculating Quantity-to-Age Ratios

Created a new column by dividing the quantity purchased by the customer's age.

**Importance:** This exercise demonstrates how to calculate ratios between numerical columns. Ratios help express relationships between different measurements, although the business usefulness of a quantity-to-age ratio requires careful interpretation.

### 4. Calculating Sales per Item

Calculated the average sales amount per item by dividing each transaction's total amount by the quantity purchased.

**Importance:** This helps evaluate revenue generated per unit sold and can be used to verify pricing calculations or identify inconsistencies in transaction data.

### 5. Calculating Adjusted Sales

Created an adjusted sales column by increasing the original transaction amount by 10%.

**Importance:** This demonstrates how businesses can model hypothetical price changes, estimate revised revenue, and evaluate different pricing scenarios.

### 6. Calculating Each Transaction's Percentage of Total Sales

Calculated the contribution of individual transactions to overall sales revenue by dividing each transaction amount by total revenue and multiplying by 100.

**Importance:** Percentage-of-total calculations help identify the relative contribution of individual transactions, compare sales values, and understand revenue distribution.

### 7. Calculating Quantity Percentages

Calculated the percentage contribution of each transaction's quantity to the total number of items sold.

**Importance:** This provides insight into how product quantities are distributed across transactions and helps distinguish sales volume from monetary sales performance.

### 8. Comparing Customer Age with Average Age

Created an age ratio by dividing each customer's age by the average customer age.

**Importance:** This introduces the use of statistical functions such as `mean()` within transformation formulas. The resulting ratio helps identify observations above or below the dataset average.

## Pandas Functions and Techniques Practiced

| Function or technique | Purpose | Importance |
|---|---|---|
| `pd.read_csv()` | Loads CSV data into a DataFrame | Enables analysis of structured datasets |
| `df['column']` | Selects or creates columns | Supports feature engineering and data manipulation |
| `sum()` | Calculates totals | Essential for revenue and quantity analysis |
| `mean()` | Calculates averages | Supports comparisons against typical values |
| Arithmetic operations | Performs multiplication, division, and addition | Enables calculations of business metrics |
| Parentheses `()` | Groups mathematical expressions | Improves readability and calculation accuracy |
| `head()` | Displays the first few rows | Helps inspect and validate transformed data |

## Key Learning Outcomes

Through this project, I developed a better understanding of:

- **Feature Engineering:** Creating new variables from existing dataset columns.
- **Data Manipulation:** Applying mathematical operations directly to Pandas DataFrames.
- **Percentage Analysis:** Understanding the contribution of individual observations to dataset totals.
- **Ratio Analysis:** Comparing numerical values to identify relationships.
- **Statistical Transformations:** Using aggregation functions within row-level calculations.
- **Data Validation:** Checking calculated values and identifying potential errors in transformation logic.
- **Code Readability:** Structuring calculations across multiple lines to improve maintainability.

## Conclusion

This project strengthened my practical understanding of **data transformation using Python and Pandas**. By working with retail sales transactions, I learned how to convert raw numerical values into additional analytical features that can support business reporting and exploratory data analysis.

These foundational skills are important for progressing toward more advanced tasks in **Data Analysis, Data Science, and Data Engineering**, including data cleaning, feature engineering, exploratory analysis, and preparing datasets for visualization and machine learning.
