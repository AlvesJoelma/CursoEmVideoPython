#n= (input("Digite um numero 0 a 9999: "))
#print("Unidade", n[3])
#print("Dezenha", n[2])
#print("Centena", n[1])
#print("Milhar", n[0])

n= int(input("Digite um numero 0 a 9999: "))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print(u)
print(d)
print(c)
print(m)