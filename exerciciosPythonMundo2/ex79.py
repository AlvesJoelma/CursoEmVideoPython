numeros = list()
while True:
    n = int(input('Digite um valor'))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Não vou adcionar...')
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
numeros.sort()
print(f'Você adcionou os valores {numeros}.')