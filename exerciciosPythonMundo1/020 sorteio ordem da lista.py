import random
a1= input("Primeiro aluno")
a2= input("Segundo")
a3= input("Terceiro")
a4= input("Quarto")
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print(lista)