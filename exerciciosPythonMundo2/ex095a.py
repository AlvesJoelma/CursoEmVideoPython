time = []
jogador = dict()
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos  gols fez na partida {c+1}? ')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
            print('ERRO. Digite apenas S ou N.')
    if resp == 'N':
        break
print('*' * 40)
print(f'{"cod":<4}{"nome":<10}{"gols":<10}{"total":<4}')




print('*'*40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')