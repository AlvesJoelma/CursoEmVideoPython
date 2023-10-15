numeros = []
while True:
    numeros.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Os numeros digitados foram {numeros}')
print(f'Você digitou {len(numeros)} numeros.')
numeros.sort(reverse=True)
print(f'Numeros em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O numero 5 foi digitado')
else:
    print('O numero 5 não foi digitado')