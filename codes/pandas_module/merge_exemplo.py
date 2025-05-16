import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 3], 'valor': [10, 20, 30]})
df2 = pd.DataFrame({'id': [2, 3, 4], 'categoria': ['A', 'B', 'C']})

df_merged = pd.merge(df1, df2, on='id', how='outer')

print(df_merged)
