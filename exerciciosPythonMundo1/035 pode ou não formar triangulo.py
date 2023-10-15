r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("Os segmentos acima \033[1;32;43m PODEM \033[m formar triângulo")
else:
    print("Os segmentos acima \033[1;31;43m NÃO PODEM \033[m formar triangulos")