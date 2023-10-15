matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = maior = somacoluna =0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))

for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz [l][c]}',end=' ')
        if matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]
    print()
print(f'A soma dos valores é {soma}')
for l in range(0,3):
    somacoluna = somacoluna + matriz[l][2]
print(f'A soma da terceira coluna é {somacoluna}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da coluna 2 é {maior}')