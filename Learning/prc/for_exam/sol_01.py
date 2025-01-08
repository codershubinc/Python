''' 
Q1. Create a Pandas Series from a list of integers [10, 20, 30, 40, 50] and assign it to a variable s. 

Change the index of the Series to ['a', 'b', 'c', 'd', 'e']. 

Retrieve the element at index 'c'. 

Calculate the sum of all elements in the Series. 

Print the updated Series and the sum. 
'''

import pandas as pd  #type: ignore



s = pd.Series([10, 20, 30, 40, 50])
s.index = ['a', 'b', 'c', 'd', 'e']

print( 'The element at index c is' ,  s['c']) 
print('Sum of the series is ' , s.sum())
print( 'Updated series is ' , s)
