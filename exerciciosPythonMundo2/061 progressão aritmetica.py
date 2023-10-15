primeiro = int(input("Primeiro termo"))
razao = int(input("Segundo termo"))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end=' ')
    termo = termo + razao
    cont = cont + 1