n = int(input("Digite quantos termos quer mostrar"))
t1 = 0
t2 = 1
print(t1,t2, end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    cont = cont + 1
print("FIM")
