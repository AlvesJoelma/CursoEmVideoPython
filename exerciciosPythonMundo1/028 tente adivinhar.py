import random
from time import sleep
computador = random.randint(0,5)
aposta= int(input("O computador pensara em um numero de 0 a 5.\nTente adivinhar. Faça sua aposta: "))
print("=*="*15)
print("Processando...")
sleep(3)
if aposta == computador:
    print("Parabens, você venceu. O computador pensou em ", computador)
else:
    print("Você perdeu. O computador pensou no numero ", computador)