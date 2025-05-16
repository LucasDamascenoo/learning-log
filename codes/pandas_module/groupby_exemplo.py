import pandas as pd

dados = {
    'Categoria': ['A', 'A', 'B', 'B', 'C'],
    'Valor': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(dados)

agrupado = df.groupby('Categoria')['Valor'].sum()

print(agrupado)
