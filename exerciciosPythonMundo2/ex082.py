lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp not in 'NS':
        resp = str(input('Resposta invalida. Deseja continuar? [S/N] '))
    elif resp in 'Nn':
        break
print(f'Os numeros digitados foram {lista}')
print(f'Os numeros pares digitados foram {pares}')
print(f'Os numeros impares digitados foram {impares}')