'''
Q4. Create a Pandas DataFrame from the following data: 

“data = {'CustomerID': [1, 2, 3, 4, 5], 'Purchase': [250, None, 150, 300, None]}” 

Assign the DataFrame to a variable df. 

Replace the missing values in the Purchase column with the average value of the column. 

Group the DataFrame by CustomerID and calculate the total purchase amount for each customer. 

Print the cleaned DataFrame and the grouped DataFrame with total purchase amounts. 
'''

import pandas as pd #type: ignore

data = {'CustomerID': [1, 2, 3, 4, 5], 'Purchase': [250, None, 150, 300, None]}

df = pd.DataFrame(data)
print('DataFrame is \n', df)

df['Purchase'] = df['Purchase'].fillna(df['Purchase'].mean())

print('Updated DataFrame is \n', df)

grouped_df = df.groupby('CustomerID')['Purchase'].sum()

print('Grouped DataFrame is \n', grouped_df)