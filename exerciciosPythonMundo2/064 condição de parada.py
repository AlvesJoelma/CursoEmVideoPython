cont = 0
soma = 0
num = 0
num = int(input("Digite um numero"))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input("Digite um numero"))
print("Foram digitados", cont)
print("A soma dos numeros é", soma)