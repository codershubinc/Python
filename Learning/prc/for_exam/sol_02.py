"""
Q2. Create a Pandas Series from a dictionary {'A': 5, 'B': 10, 'C': 15, 'D': 20, 'E': 25}. 

Add 5 to each element in the Series. 

Find the maximum value in the Series. 

Filter and display only the elements that are greater than 15. 

Print the final Series and the maximum value. 

"""

import pandas as pd

s = pd.Series({'A': 5, 'B': 10, 'C': 15, 'D': 20, 'E': 25})
s = s + 5

print( 'Updated series is \n ' ,  s[s > 15])

print('Maximum value is ' , s.max())

