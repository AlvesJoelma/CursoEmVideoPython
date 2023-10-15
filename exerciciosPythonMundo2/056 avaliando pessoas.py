somaidade = 0
maisvelho = 0
nomemaisvelho = ''
totmulher = 0
for p in range(1,5):
    print(p, "° Pessoa")
    nome= input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F").upper()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maisvelho = p
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher = totmulher +1

media= somaidade / 4
print("A média de idades é", media)
print("O homem mais velho tem", maisvelho, " anos e se chama", nomemaisvelho)
print('O total de mulheres menor de 20 naos é ', totmulher)