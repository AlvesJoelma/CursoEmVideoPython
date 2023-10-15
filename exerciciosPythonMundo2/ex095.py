jog = {}
partidas = []
time = []
while True:
    jog.clear()
    jog['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols fez na partida {c+1}? ')))
        jog['gols'] = partidas[:]
        jog['total'] = sum(partidas)
    time.append(jog.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
            print('ERRO. Digite apenas S ou N.')
    if resp == 'N':
        break
print('-*'*30)
print(f'{"cod":<4}{"nome":<10}{"gols":<10}{"total":<4}')
for k, v in enumerate(time):
    print(f'{k+1:<4}{v[0]}{jog["gols"]:<10}{jog["total"]:<4}')
