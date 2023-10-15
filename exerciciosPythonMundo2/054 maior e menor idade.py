from datetime import date
atual= date.today().year
menor = 0
maior = 0
for c in range(1,8):
    nasc = int(input("Data de nascimento: "))
    idade = atual - nasc
    if idade >= 21:
        maior= maior + 1
    else:
        menor = menor + 1
print('Foram digitados', maior, " pessoas maiores de idade e ", menor, "pessoas menos de idade")
