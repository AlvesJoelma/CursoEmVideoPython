primeiro = int(input("Primeiro termo"))
razao = int(input("Segundo termo"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' ')
        termo = termo + razao
        cont = cont + 1
    print("Pausa")
    mais= int(input("Quantos termos a mais você quer mostrar"))
print("Fim")