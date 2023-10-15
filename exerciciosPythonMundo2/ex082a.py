lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp not in 'NS':
        resp = str(input('Resposta invalida. Deseja continuar? [S/N] '))
    elif resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os numeros digitados foram {lista}')
print(f'Os numeros pares digitados foram {pares} ')
print(f'Os numeros impares digitados foram {impares} ')
