
# entrada_tabuada = int(input('qual numero deseja fazer a  tabuada? '))

# for numero in range(1, 11):
#     print(f'{entrada_tabuada} x {numero} = {entrada_tabuada * numero}')


# fatorial

n = int(input('digite um numero: '))
fatorial = 1

for i in range(1, n + 1):
  fatorial = fatorial * i

print(f'fatorial de {n} eh {fatorial}')
