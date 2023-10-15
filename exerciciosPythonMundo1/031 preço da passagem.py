distancia = int(input("Quantos Km serão percorridos? "))
if distancia <=200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print("A passagem custara R$ ", preço)