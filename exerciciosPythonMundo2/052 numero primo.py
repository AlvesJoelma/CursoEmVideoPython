n = int(input("Digite um numero"))
tot = 0
for c in range(1, n + 1): #+1 pq o for exclui o ultiimo
    if n % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[33m', end='')
    print(c)
print("\33[mO numero ", n, " foi divisivel ", tot, " vezes")
if tot == 2:
    print("Por isso ele É PRIMO")
else:
    print("Por isso ele NÃO É PRIMO")
