import pandas as pd
import numpy as np

''' comment starts here
dic = {
    'Name': ['a','c','b','d','a'],
    'Gender': ['M','M','F','F','M'],
    'Score': [1,2,3,4,5]
}


df = pd.DataFrame(dic) # type casting

print(df)
print(type(df))

grouped_df = df.groupby('Name')

print("grouped_df <|<==================================================================>|>")

# print(grouped_df.head(9))
# print(grouped_df.first())
# print(grouped_df.last())
# print(grouped_df.agg(np.median))    

print("grouped_df score.agg(np.size) <|<==================================================================>|>")
print(grouped_df['Score'].agg(np.size))

print(grouped_df['Score'].agg(np.sum))
print(grouped_df['Score'].agg( [np.mean , np.std]).rename( columns={'mean':'mean_score', 'std':'std_score'}))

comments end here
'''

data = {
    'Name': ['a', 'c', 'b', 'd', 'a'],
    'Score': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)  # type casting

def f(x):
        return x * x


df['Score'] = df['Score'].apply(f)

print(df)
