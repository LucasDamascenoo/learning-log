import pandas as pd

dados = {'A': [1, 2, None, 4], 'B': [None, 2, 3, 4]}

df = pd.DataFrame(dados)

df_preenchido = df.fillna(0)

print(df_preenchido)
