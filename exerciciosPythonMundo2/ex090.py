dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
print('*'*24)
print(f'O nome é {dados["nome"]}')
print(f'A média é {dados["média"]}')
if dados['média'] >= 7:
    print('O aluno está \033[32mAPROVADO')
elif 5 <= dados['média'] < 7:
    print('O aluno esta em \033[33mRECUPERAÇÃO')
else:
    print('O aluno está \033[31mREPROVADO')