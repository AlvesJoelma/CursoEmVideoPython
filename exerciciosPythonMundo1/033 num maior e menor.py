a = int(input("Primeiro numero"))
b = int(input("Segundo numero"))
c = int(input("Terceiro numero"))
# maior numero
#maior = a e posso excluir o primeiro if
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>b and c>a:
    maior = c
#menor numero
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c

print("menor numero é ", menor, " e o maior numero é ", maior)
