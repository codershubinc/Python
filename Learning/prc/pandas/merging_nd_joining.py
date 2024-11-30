

import pandas as pan

df1 = pan.DataFrame(
    {
        "ID":[487,345,455,563,453],
        "Name":["sam", "tom", "joe", "jim", "bob"],
        "Age":[32,33,34,35,36],
    }
)

df2 = pan.DataFrame(
    {
        "ID":[487,345,455,563,453],
        "Name":["sam", "tom", "joe", "jim", "bob"],
        "Age":[32,33,34,35,36],
    }
)

print(df1)
print(df2)

df3 = df1.merge(df2, how='outer', on='ID')

print(df3)