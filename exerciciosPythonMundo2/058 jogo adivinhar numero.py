import random
from time import sleep
computador = random.randint(0,10)
print("Vou pensar em numero de 0 a 10")
acertou = False
cont = 0
while not acertou:
    aposta = int(input("Faça sua aposta: "))
    cont = cont + 1
    if aposta == computador:
        acertou = True
    else:
        if aposta < computador:
            print("Tente um valor mais alto.")
        else:
            print("Tente um valor menor")

print("Parabens, você venceu. O computador pensou em ", computador)
print("Voce precisou de ", cont, " tentativas")