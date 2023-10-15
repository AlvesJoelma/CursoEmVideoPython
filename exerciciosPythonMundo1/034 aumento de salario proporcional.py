atual = float(input("Qual seu salário atual: R$ "))
if atual >= 1250:
    novo =atual + (atual * 10 / 100)
else:
    novo = atual + (atual * 15 / 100)
print("Seu novo salário sera de R$ ", novo)
