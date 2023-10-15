from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
print('*'*28)
print('         MEGA SENA')
print('*'*28)
qtdd = int(input('Quantos  jogos deseja fazer? '))
tot = 1
while tot <= qtdd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(' '*3, f'SORTEANDO {qtdd} JOGOS', '  '*3)
for i , l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('--------- Boa sorte ---------')