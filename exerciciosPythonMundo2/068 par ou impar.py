import random
v = 0
print("Vamos jogar par ou impar!")
print("=-"*15)
while True:
    jogador = int(input("Digite um numero: "))
    computador = random.randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Impar? [P/I]")).upper()[0].strip()
    print("Voce jogou", jogador, " e o computador ", computador, "A soma dos valores é ", total)
    print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")
    if tipo ==  "P":
        if total % 2 == 0:
            print('Voce VENCEU')
            v = v + 1
        else:
            print("Voce PERDEU")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Voce VENCEU")
            v = v + 1
        else:
            print("Voce PERDEU")
            break
    print("Vamos jogar novamente")
print("GAME OVER. Voce VENCEU", v, "vezes")
