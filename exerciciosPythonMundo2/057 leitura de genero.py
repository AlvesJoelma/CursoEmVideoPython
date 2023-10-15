sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados invalidos. Por favor digite novamente [M/F]: ")).strip().upper()[0]
print(sexo, ' registrado com sucesso')
print("acabou")