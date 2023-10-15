listanum = []
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'Os valores digitados foram {listanum}')
print(f'O maior valor digitado foi {max(listanum)} na posição {listanum.index(max(listanum))}')
print(f'O menor valor digitado foi {min(listanum)} na posição {listanum.index(min(listanum))}')