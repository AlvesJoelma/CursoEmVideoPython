maioridade= homens = totmulheres =  0
while True:
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input("Sexo [M/F]: ")).upper()[0].strip()
    if idade >= 18:
        maioridade = maioridade + 1
    if sexo == 'Mm':
        homens = homens + 1
    if sexo == "Ff" and idade < 20:
        totmulheres = totmulheres + 1
    resp = " "
    while resp not in 'SN':
        resp = input("Deseja continuar? [S/N]").upper()[0].strip()
    if resp == "N":
            break
print("Total de pessoas maior de 18 anos: ", maioridade)
print("Total de homens cadastrados: ", homens)
print("Total de mulheres com menos de 20 anos", totmulheres)

