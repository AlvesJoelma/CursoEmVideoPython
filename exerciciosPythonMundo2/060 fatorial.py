n = int(input("Digite um numero para calcular seu fatorial: "))
c = n
f = 1
while c > 0:
    print(c, end='')
    print('x' if c > 1 else "=")
    f = f * c
    c = c-1
print("O fatorial é ", f)