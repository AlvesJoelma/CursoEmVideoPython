valores = [int(input('Digite um valor na posição 0: ')),
           int(input('Digite um valor na posição 1: ')),
           int(input('Digite um valor na posição 2: ')),
           int(input('Digite um valor na posição 3: ')),
           int(input('Digite um valor na posição 4: '))]
print(f'O valores digitados foram {valores}')
for cont, v in enumerate(valores):
    print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}')
    print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')
    break