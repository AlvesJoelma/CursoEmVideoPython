dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
if dados['média'] >= 7:
    dados['situação'] = 'APROVADO'
elif 5 <= dados['média'] < 7:
    dados['situação'] = 'RECUPERAÇÃO'
else:
    dados['situação'] =  'REPROVADO'
print('*'*24)
for k, v in dados.items():
    print(f'{k} é igial a {v}')