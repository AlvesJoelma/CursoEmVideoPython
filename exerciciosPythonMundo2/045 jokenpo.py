import random
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = random.randint(0,2)
print('''SUAS OPÇÕES
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual sua jogada?"))
print("*="*15)
print("JOKENPO!!!")
sleep(2)
print("*="*15)
print("Computador escolheu ", (itens[computador]))
print("Voce escolheu", (itens[jogador]))
if computador == 0: #pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada invalida")

elif computador == 1: #papel
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("Jogada invalida")
elif computador == 2: #tesoura
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada invalida")
