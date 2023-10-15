maior = 0
menor = 0
for p in range(0,5):
    peso= float(input("Digite o peso:"))
    if p == 1:
        maior = p
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("O maior peso foi ", maior, " e o menoor peso foi ", menor)