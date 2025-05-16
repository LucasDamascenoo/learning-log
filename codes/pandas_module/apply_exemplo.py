import pandas as pd

dados = {'A': [1, 2, 3, 4]}

df = pd.DataFrame(dados)

df['A_dobrado'] = df['A'].apply(lambda x: x * 2)

print(df)
