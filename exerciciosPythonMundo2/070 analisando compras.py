print("           LOJA JS")
print("*-"*15)
resp = "S"
total = maisdemil = maisbarato = cont = nomebarato = 0
while True:
    produto = input("Produto: ").upper()
    preço = float(input("Preço: R$ "))
    cont += 1
    total += preço
    if preço > 1000:
        maisdemil += 1
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        nomebarato = produto
#    else:
#       if preço < maisbarato:
#            maisbarato = preço
#            nomebarato = produto
    resp = " "
    while resp not in "SN":
        resp = input("Deseja continuar? [S/N]").upper()[0].strip()
    if resp in "Nn":
        break


print("Total gasto: R$ ", total)
print("Produtos com valor acima de R$ 1000,00: ", maisdemil)
print("O produto mais barato foi", nomebarato, "custando ", maisbarato)