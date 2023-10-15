geral = []
dados = {}
soma = média = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO. Digite M ou F')
    dados['idade'] = int(input('Idade: '))
    geral.append(dados.copy())
    soma = soma + dados['idade']
    média = soma / len(geral)
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break


print(geral)
print('*-'*20)
print(f'Foram cadastradas {len(geral)} pessoas')
print('*-'*20)
print(f'A média da idade é {média}')
print('*-'*20)
print(f'As mulheres são ',end='')
for p in geral:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}',end=' ')
print()
print('*-'*20)
print('Lista de pessoas com idade acima da média ')
for p in geral:
    if p['idade'] >= média:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v};',end=' ')
