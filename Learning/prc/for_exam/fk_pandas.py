import pandas as pd
'''Practice Questions 

Topic#1: Pandas Series and DataFrame 



Q1. Create a Pandas Series from a list of integers [10, 20, 30, 40, 50] and assign it to a variable s. 

Change the index of the Series to ['a', 'b', 'c', 'd', 'e']. 

Retrieve the element at index 'c'. 

Calculate the sum of all elements in the Series. 

Print the updated Series and the sum. '''
"""

s = pd.Series([10, 20, 30, 40, 50])
s.index = ['a', 'b', 'c', 'd', 'e']
print(s['c'])
"""


'''Q2. Create a Pandas Series from a dictionary {'A': 5, 'B': 10, 'C': 15, 'D': 20, 'E': 25}. 

Add 5 to each element in the Series. 

Find the maximum value in the Series. 

Filter and display only the elements that are greater than 15. 

Print the final Series and the maximum value. '''

'''
Q3. Create a Pandas DataFrame from the following data: 

“data = {'Product': ['A', 'B', 'C', 'D'], 'Price': [100, 150, 200, 250], 'Quantity': [10, 15, 20, 25]}” 

Assign the DataFrame to a variable df. 

Calculate the total sales for each product (Price * Quantity) and add it as a new column TotalSales. 

Find the product with the highest total sales. 

Display the DataFrame sorted by TotalSales in descending order. 

Print the updated DataFrame and the product with the highest total sales. 
'''

data = {'Product': ['A', 'B', 'C', 'D'], 'Price': [100, 150, 200, 250], 'Quantity': [10, 15, 20, 25]}
df = pd.DataFrame(data)
df['TotalSales'] = df['Price'] * df['Quantity']
print(df.sort_values('TotalSales', ascending=False))
print(df.loc[df['TotalSales'].idxmax()])