"""
The structure data = {'amount': [total_crypto_savings, total_shares_savings]} is a Python dictionary that defines a single-column DataFrame. Here's a breakdown of this structure:

Key ('amount'): This is the column name for the DataFrame. In this case, the DataFrame will have one column named 'amount'.
Value ([total_crypto_savings, total_shares_savings]): This is a list containing the data values that will populate the 'amount' column in the DataFrame. The list [total_crypto_savings, total_shares_savings] provides the values for each row of the DataFrame.
When you use this dictionary to create a DataFrame with pd.DataFrame(data), the keys become column names, and the corresponding values become the data in each column. In this case, it creates a DataFrame with a single column named 'amount', where each row contains a value from the list [total_crypto_savings, total_shares_savings].

Here's a step-by-step breakdown:

Column Name: 'amount'
Data Values:
Row 1: total_crypto_savings
Row 2: total_shares_savings
When you pass this dictionary to pd.DataFrame(), it creates a DataFrame structured like this:

"""