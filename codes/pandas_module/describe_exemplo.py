import pandas as pd

dados = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}

df = pd.DataFrame(dados)

print(df.describe())
