s= 0
cont = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s= s + c
        cont= cont + 1
        print(c)
print("A soma é ", s, " foram somados ", cont)