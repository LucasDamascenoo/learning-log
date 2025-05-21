
# # verificacao do input da nota

# nota = float(input('digete uma nota: '))


# while True:
#   if nota < 0 or nota > 10 :
#     print('nota invalida,insira a nota correta')
#     nota = float(input('digete uma nota: '))
#   else:
#     print('nota inserida')
#     break



# numero misterioso

import random

numero = 30

chute = int(input(' adivinhe o valor: '))

while chute != numero:
  if chute > numero:
    print('seu numero eh maior que o numero')
    chute = int(input(' adivinhe o valor: '))
  else:
    print('seu numero eh menor que o chute')
    chute = int(input(' adivinhe o valor: '))

print(f'parabens vc acertou, o numero era {numero}')

