# %%

import pandas as pd
import kagglehub
# %%
dados = {
    'Loja': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Ano': [2023, 2024, 2023, 2024, 2023, 2024],
    'Vendas': [2500, 2700, 3000, 3100, 2000, 2200]
}


df = pd.DataFrame(dados)

df['Categoria'] = ['Eletrônico', 'Eletrônico',
                   'Móveis', 'Móveis', 'Eletrônico', 'Eletrônico']


# %%

valor_por_loja = df.pivot_table(

    values='Vendas',
    index=['Loja', 'Categoria'],
    columns='Ano',
    aggfunc=sum

)

valor_por_loja

Loja -
