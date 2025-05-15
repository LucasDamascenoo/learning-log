
import pandas as pd
from pathlib import Path

# 📥 Caminho do arquivo de origem
caminho_origem = Path.home() / 'Downloads' / 'clientes.xlsx'

# 📖 Ler o Excel
df = pd.read_excel(caminho_origem)
print(df.head())

# 📁 Caminho da nova pasta
nova_pasta = Path.home() / 'Downloads' / 'Relatorios'

# 📌 Verificar e criar a pasta se não existir
if not nova_pasta.exists():
    nova_pasta.mkdir(parents=True)
    print(f'Pasta criada: {nova_pasta}')
else:
    print(f'A pasta já existe: {nova_pasta}')

# 📤 Caminho do novo arquivo
caminho_novo_arquivo = nova_pasta / 'relatorio_clientes.xlsx'

# 💾 Salvar o DataFrame em Excel
df.to_excel(caminho_novo_arquivo, index=False)

print(f'Arquivo salvo em: {caminho_novo_arquivo}')
