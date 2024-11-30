import pandas as pan

df = pan.read_csv('data.csv')
df = pan.DataFrame(
    {
        "ID":[487,345,455,563,453],
        "Name":["sam", "tom", "joe", "jim", "bob"],
        "Age":[32,33,34,35,36],
    }
)
print(df)