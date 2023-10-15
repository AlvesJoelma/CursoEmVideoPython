n1 = int(input("Primeiro valor"))
n2 = int(input("Segundo valor"))
resp = 0

while resp != 5:
    print('''Opçoes
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos numeros
            [5]sair do programa''')
    resp = int(input("Escolha uma opção"))

    if resp == 1:
        soma = n1 + n2
        print("A soma é ", soma)
    elif resp == 2:
        multiplicar = n1 * n2
        print("A multiplicação é ", multiplicar)
    elif resp == 3:
        if n1 > n2:
            print("O maior numero é ", n1)
        else:
            print("O maior numero é ", n2)
    elif resp == 4:
        n1 = int(input("Primeiro valor"))
        n2 = int(input("Segundo valor"))
    elif resp== 5:
        break
    else:
        print("Opção Invalida")
    print("*==*" * 15)

print("Programa Finalizado")

