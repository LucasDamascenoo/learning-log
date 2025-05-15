import os
from datetime import datetime


folder = './logs/'

if not os.path.exists(folder):
    os.makedirs(folder)


today = datetime.now().strftime('%Y-%m-%d')
file_name = f'{folder}/{today}.md'

content = f"""# 📚 {today}

## ✅ O que estudei hoje
- 

## 💡 Aprendizados
- 

## ❓ Dúvidas
- 

## 🔗 Links úteis
- 

## 📌 Observações
- 
"""


if not os.path.exists(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"✅ Log criado: {file_name}")
else:
    print(f"⚠️ Log de hoje já existe: {file_name}")
