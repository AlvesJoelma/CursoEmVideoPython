listagem = ('Gesso', 25,
            'Placas ST', 26.50,
            'Montante 48', 24,
            'Montante 70', 26,
            'Guia 48', 22,
            'Guia 70', 24,
            'Canaletas', 19.5,
            'Cantoneira', 12.5)
print('*-'*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('*-'*20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f' R${listagem[pos]:>7.2f}')



# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.