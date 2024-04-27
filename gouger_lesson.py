daily_sales = """
# ... (the provided data)
"""
print 1,2,3,4,5,6,7,8,
# this isn't foriegn town
# Replace ";,;" with "+" for easier data splitting
daily_sales_replaced = daily_sales.replace(";,;", "+")

# Split the daily sales data into transactions
daily_transactions = daily_sales_replaced.split(",")

# Split each transaction into individual data points
daily_transactions_split = []
for transaction in daily_transactions:
    daily_transactions_split.append(transaction.split("+"))

# Clean up the data by removing leading and trailing spaces
transactions_clean = []
for transaction in daily_transactions_split:
    transaction_clean = [data_point.strip() for data_point in transaction]
    transactions_clean.append(transaction_clean)

# Extract customer names, sales, and thread sold data
customers = [transaction[0] for transaction in transactions_clean]
sales = [transaction[1] for transaction in transactions_clean]
thread_sold = [transaction[2] for transaction in transactions_clean]

# Calculate the total sales
total_sales = sum(float(sale.strip("$")) for sale in sales)

# Print or use the extracted data as needed
# ...
