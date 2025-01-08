'''Q3. Create a Pandas DataFrame from the following data: 

“data = {'Product': ['A', 'B', 'C', 'D'], 'Price': [100, 150, 200, 250], 'Quantity': [10, 15, 20, 25]}” 

Assign the DataFrame to a variable df. 

Calculate the total sales for each product (Price * Quantity) and add it as a new column TotalSales. 

Find the product with the highest total sales. 

Display the DataFrame sorted by TotalSales in descending order. 

Print the updated DataFrame and the product with the highest total sales. 


'''

import pandas as pd #type: ignore

data = {'Product': ['A', 'B', 'C', 'D'], 'Price': [100, 150, 200, 250], 'Quantity': [10, 15, 20, 25]}

df = pd.DataFrame(data)

print('DataFrame is \n', df)

df['TotalSales'] = df['Price'] * df['Quantity']

print('Updated DataFrame is \n', df)

print('Product with highest total sales is \n', df.loc[df['TotalSales'].idxmax()])   
#  df.loc => is for selecting rows and columns by label/index
#  df['TotalSales'].idxmax() => returns the index of the first occurrence of the maximum value in the Series.
#  df.loc[df['TotalSales'].idxmax()] => returns the row with the maximum TotalSales

print('DataFrame sorted by TotalSales in descending order is \n', df.sort_values('TotalSales', ascending = False))

