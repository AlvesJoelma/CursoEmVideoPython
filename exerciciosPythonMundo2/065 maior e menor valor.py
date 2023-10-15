resp = "S"
cont = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input("Digite um numero"))
    cont = cont +1
    soma = soma + n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input("Deseja continuar? [S/N]")
media = soma / cont
print("A média dos numeros digitados é ", media)
print("O maior numero foi", maior, ' e o menor foi', menor)
