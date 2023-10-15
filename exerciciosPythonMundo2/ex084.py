galera = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()

    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break

print(f'Foram cadastradas {len(galera)} pessoas.')

print(f'O maior peso foi {maior:} kg. Peso de ',end=' ')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}.')
print(f'O menor peso foi {menor} Kg. Peso de ',end=' ')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}.')